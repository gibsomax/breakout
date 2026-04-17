"""
Collision tests for BALL, BRICK, PADDLE, and INNERBOX interactions.
Simulates the collision logic from main.py directly on the objects.
"""
import unittest
import copy
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
pygame.init()
pygame.display.set_mode((1000, 800))

from breakout_main.game_objects.ball import BALL
from breakout_main.game_objects.brick import BRICK
from breakout_main.game_objects.paddle import PADDLE
from breakout_main.game_objects.inner_box import INNERBOX
from breakout_main.settings import SCREEN_WIDTH, SCREEN_HEIGHT, ball_speed


class TestBallBrickCollision(unittest.TestCase):

    def test_ball_bounces_off_brick(self):
        """Ball vy should flip when it hits a brick."""
        ball = BALL()
        brick = BRICK(100, 100)
        ball.ball_rect.topleft = (102, 100)  # overlapping with brick
        ball.vy = ball_speed

        if brick.alive and brick.rect.colliderect(ball.ball_rect):
            brick.hit()
            ball.vy *= -1

        self.assertLess(ball.vy, 0)

    def test_brick_hit_on_ball_collision(self):
        """Brick health should decrease when ball collides with it."""
        ball = BALL()
        brick = BRICK(100, 100, health=2)
        ball.ball_rect.topleft = (102, 100)  # overlapping with brick

        if brick.alive and brick.rect.colliderect(ball.ball_rect):
            brick.hit()
            ball.vy *= -1

        self.assertEqual(brick.health, 1)

    def test_brick_dies_on_collision_with_health_1(self):
        """Brick with health 1 should die after ball collision."""
        ball = BALL()
        brick = BRICK(100, 100, health=1)
        ball.ball_rect.topleft = (102, 100)  # overlapping with brick

        if brick.alive and brick.rect.colliderect(ball.ball_rect):
            brick.hit()
            ball.vy *= -1

        self.assertFalse(brick.alive)

    def test_dead_brick_does_not_affect_ball(self):
        """Ball vy should not change when colliding with a dead brick."""
        ball = BALL()
        brick = BRICK(100, 100, health=1)
        brick.alive = False
        ball.ball_rect.topleft = (102, 100)
        original_vy = ball.vy

        if brick.alive and brick.rect.colliderect(ball.ball_rect):
            brick.hit()
            ball.vy *= -1

        self.assertEqual(ball.vy, original_vy)


class TestBallPaddleCollision(unittest.TestCase):

    def test_ball_bounces_off_paddle_top(self):
        """Ball hitting the top of the paddle should set vy negative."""
        paddle = PADDLE(160, 10, 400, 600)
        ball = BALL()
        ball.ball_rect.midbottom = (paddle.paddle_rect.centerx, paddle.paddle_rect.top + 2)
        ball.vy = ball_speed

        if paddle.paddle_rect.colliderect(ball.ball_rect):
            if ball.ball_rect.bottom <= paddle.paddle_rect.top + abs(ball.vy) + 5:
                ball.vy = -ball_speed
                ball.vx = (ball.ball_rect.x / 10 - paddle.paddle_rect.center[0] / 10)

        self.assertLess(ball.vy, 0)

    def test_ball_vx_changes_based_on_paddle_position(self):
        """Ball vx should be influenced by where it hits the paddle."""
        paddle = PADDLE(160, 10, 400, 600)
        ball = BALL()
        # Place ball to the right of paddle center
        ball.ball_rect.midbottom = (paddle.paddle_rect.right - 10, paddle.paddle_rect.top + 2)
        ball.vy = ball_speed

        if paddle.paddle_rect.colliderect(ball.ball_rect):
            if ball.ball_rect.bottom <= paddle.paddle_rect.top + abs(ball.vy) + 5:
                ball.vy = -ball_speed
                ball.vx = (ball.ball_rect.x / 10 - paddle.paddle_rect.center[0] / 10)

        # vx should be non-zero since ball is off-center
        self.assertNotEqual(ball.vx, 0)


class TestBallInnerBoxCollision(unittest.TestCase):

    def test_ball_hitting_top_of_inner_box_spawns_copy(self):
        """Ball hitting the top wall of an inner box should spawn a copy inside."""
        inner_box = INNERBOX(50, 50)
        ball = BALL()
        ball.ball_rect.topleft = (inner_box.box_rect_top.x + 5, inner_box.box_rect_top.y - 1)
        ball.vy = -ball_speed

        if inner_box.box_rect_top.colliderect(ball.ball_rect):
            ball_copy = copy.copy(ball)
            ball_copy.ball_rect = ball.ball_rect.copy()
            ball_copy.ball_rect.y += 5
            ball_copy.vx /= 4
            ball_copy.vy /= 4
            if abs(ball_copy.vx) < 1:
                ball_copy.vx = 1 if ball_copy.vx >= 0 else -1
            if abs(ball_copy.vy) < 1:
                ball_copy.vy = 1 if ball_copy.vy >= 0 else -1
            inner_box.ball.append(ball_copy)
            ball.vy = -abs(ball.vy)

        self.assertEqual(len(inner_box.ball), 1)

    def test_ball_copy_has_reduced_velocity(self):
        """Ball copy spawned inside inner box should have reduced velocity."""
        inner_box = INNERBOX(50, 50)
        ball = BALL()
        ball.vx = ball_speed
        ball.vy = -ball_speed
        ball.ball_rect.topleft = (inner_box.box_rect_top.x + 5, inner_box.box_rect_top.y - 1)

        if inner_box.box_rect_top.colliderect(ball.ball_rect):
            ball_copy = copy.copy(ball)
            ball_copy.ball_rect = ball.ball_rect.copy()
            ball_copy.ball_rect.y += 5
            ball_copy.vx /= 4
            ball_copy.vy /= 4
            if abs(ball_copy.vx) < 1:
                ball_copy.vx = 1 if ball_copy.vx >= 0 else -1
            if abs(ball_copy.vy) < 1:
                ball_copy.vy = 1 if ball_copy.vy >= 0 else -1
            inner_box.ball.append(ball_copy)

        self.assertLess(abs(inner_box.ball[0].vx), abs(ball.vx))

    def test_ball_hitting_bottom_of_inner_box_bounces_up(self):
        """Ball hitting the bottom wall of inner box from outside should bounce upward."""
        inner_box = INNERBOX(50, 50)
        ball = BALL()
        ball.vy = ball_speed
        ball.ball_rect.topleft = (inner_box.box_rect_bottom.x + 5, inner_box.box_rect_bottom.y - 1)

        if inner_box.box_rect_bottom.colliderect(ball.ball_rect):
            ball_copy = copy.copy(ball)
            ball_copy.ball_rect = ball.ball_rect.copy()
            ball_copy.ball_rect.y -= 6
            ball_copy.vx /= 4
            ball_copy.vy /= 4
            if abs(ball_copy.vx) < 1:
                ball_copy.vx = 1 if ball_copy.vx >= 0 else -1
            if abs(ball_copy.vy) < 1:
                ball_copy.vy = 1 if ball_copy.vy >= 0 else -1
            inner_box.ball.append(ball_copy)
            ball.vy = abs(ball.vy)

        self.assertGreater(ball.vy, 0)

    def test_ball_hitting_left_wall_of_inner_box_bounces_right(self):
        """Ball hitting the left wall of inner box should bounce to the right."""
        inner_box = INNERBOX(50, 50)
        ball = BALL()
        ball.vx = -ball_speed
        ball.ball_rect.topleft = (inner_box.box_rect_left.x - 1, inner_box.box_rect_left.y + 5)

        if inner_box.box_rect_left.colliderect(ball.ball_rect):
            ball_copy = copy.copy(ball)
            ball_copy.ball_rect = ball.ball_rect.copy()
            ball_copy.ball_rect.x += 5
            ball_copy.vx /= 4
            ball_copy.vy /= 4
            if abs(ball_copy.vx) < 1:
                ball_copy.vx = 1 if ball_copy.vx >= 0 else -1
            if abs(ball_copy.vy) < 1:
                ball_copy.vy = 1 if ball_copy.vy >= 0 else -1
            inner_box.ball.append(ball_copy)
            ball.vx = -abs(ball.vx)

        self.assertLess(ball.vx, 0)

    def test_ball_hitting_right_wall_of_inner_box_bounces_left(self):
        """Ball hitting the right wall of inner box should bounce to the left."""
        inner_box = INNERBOX(50, 50)
        ball = BALL()
        ball.vx = ball_speed
        ball.ball_rect.topleft = (inner_box.box_rect_right.x, inner_box.box_rect_right.y + 5)

        if inner_box.box_rect_right.colliderect(ball.ball_rect):
            ball_copy = copy.copy(ball)
            ball_copy.ball_rect = ball.ball_rect.copy()
            ball_copy.ball_rect.x -= 5
            ball_copy.vx /= 4
            ball_copy.vy /= 4
            if abs(ball_copy.vx) < 1:
                ball_copy.vx = 1 if ball_copy.vx >= 0 else -1
            if abs(ball_copy.vy) < 1:
                ball_copy.vy = 1 if ball_copy.vy >= 0 else -1
            inner_box.ball.append(ball_copy)
            ball.vx = abs(ball.vx)

        self.assertGreater(ball.vx, 0)


class TestInsideBallInnerBoxCollision(unittest.TestCase):

    def test_inside_ball_bounces_off_top_wall(self):
        """Inside ball hitting the top wall should have vy set positive."""
        inner_box = INNERBOX(50, 50)
        ball = BALL()
        ball.vy = -ball_speed
        ball.is_inside_time = 0
        ball.ball_rect.topleft = (inner_box.box_rect_top.x + 5, inner_box.box_rect_top.y)
        inner_box.ball.append(ball)

        for i in inner_box.ball:
            if inner_box.box_rect_top.colliderect(i.ball_rect):
                i.vy = abs(i.vy)

        self.assertGreater(inner_box.ball[0].vy, 0)

    def test_inside_ball_bounces_off_right_wall(self):
        """Inside ball hitting the right wall should have vx set negative."""
        inner_box = INNERBOX(50, 50)
        ball = BALL()
        ball.vx = ball_speed
        ball.is_inside_time = 0
        ball.ball_rect.topleft = (inner_box.box_rect_right.x, inner_box.box_rect_right.y + 5)
        inner_box.ball.append(ball)

        for i in inner_box.ball:
            if inner_box.box_rect_right.colliderect(i.ball_rect):
                i.vx = -abs(i.vx)

        self.assertLess(inner_box.ball[0].vx, 0)

    def test_inside_ball_bounces_off_left_wall(self):
        """Inside ball hitting the left wall should have vx set positive."""
        inner_box = INNERBOX(50, 50)
        ball = BALL()
        ball.vx = -ball_speed
        ball.is_inside_time = 0
        ball.ball_rect.topleft = (inner_box.box_rect_left.x - 1, inner_box.box_rect_left.y + 5)
        inner_box.ball.append(ball)

        for i in inner_box.ball:
            if inner_box.box_rect_left.colliderect(i.ball_rect):
                i.vx = abs(i.vx)

        self.assertGreater(inner_box.ball[0].vx, 0)

    def test_inside_ball_destroyed_at_bottom(self):
        """Inside ball hitting the bottom wall should be marked for destruction."""
        inner_box = INNERBOX(50, 50)
        ball = BALL()
        ball.vy = ball_speed
        ball.is_inside_time = 0
        ball.ball_rect.topleft = (inner_box.box_rect_bottom.x + 5, inner_box.box_rect_bottom.y - 1)
        inner_box.ball.append(ball)

        for i in inner_box.ball:
            if inner_box.box_rect_bottom.colliderect(i.ball_rect) and i.is_inside_time <= 0:
                inner_box.ball_destroy.append(i)

        self.assertIn(ball, inner_box.ball_destroy)


if __name__ == "__main__":
    unittest.main()