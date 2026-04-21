"""
Basic unit tests for BALL, BRICK, and PADDLE game objects.
"""
import unittest
import os
import pygame
from breakout_main.game_objects.brick import BRICK
from breakout_main.game_objects.ball import BALL
from breakout_main.game_objects.paddle import PADDLE
from breakout_main.settings import SCREEN_WIDTH, SCREEN_HEIGHT, ball_speed
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"
pygame.init()
pygame.display.set_mode((1000, 800))


class TestBrick(unittest.TestCase):

    def test_brick_initializes_alive(self):
        """Brick should be alive on creation."""
        brick = BRICK(0, 0)
        self.assertTrue(brick.alive)

    def test_brick_hit_reduces_health(self):
        """Hitting a brick should reduce its health by 1."""
        brick = BRICK(0, 0, health=2)
        brick.hit()
        self.assertEqual(brick.health, 1)

    def test_brick_still_alive_after_one_hit_with_health_2(self):
        """Brick with health 2 should still be alive after one hit."""
        brick = BRICK(0, 0, health=2)
        brick.hit()
        self.assertTrue(brick.alive)

    def test_brick_dies_when_health_reaches_zero(self):
        """Brick should set alive to False when health hits 0."""
        brick = BRICK(0, 0, health=1)
        brick.hit()
        self.assertFalse(brick.alive)

    def test_brick_dies_after_multiple_hits(self):
        """Brick with health 3 should die after 3 hits."""
        brick = BRICK(0, 0, health=3)
        brick.hit()
        brick.hit()
        brick.hit()
        self.assertFalse(brick.alive)

    def test_brick_rect_position(self):
        """Brick rect should be set to the given x, y position."""
        brick = BRICK(100, 200)
        self.assertEqual(brick.rect.x, 100)
        self.assertEqual(brick.rect.y, 200)

    def test_brick_rect_dimensions(self):
        """Brick rect should use default width and height."""
        brick = BRICK(0, 0)
        self.assertEqual(brick.rect.width, 60)
        self.assertEqual(brick.rect.height, 20)


class TestBall(unittest.TestCase):

    def test_ball_initializes_not_destroyed(self):
        """Ball should not be marked for destruction on creation."""
        ball = BALL()
        self.assertFalse(ball.destroy)

    def test_ball_starts_near_center_x(self):
        """Ball should start near the horizontal center of the screen."""
        ball = BALL()
        self.assertAlmostEqual(ball.ball_rect.centerx, SCREEN_WIDTH * 0.5, delta=10)

    def test_ball_starts_near_bottom(self):
        """Ball should start near the bottom of the screen."""
        ball = BALL()
        self.assertAlmostEqual(ball.ball_rect.centery, SCREEN_HEIGHT * 0.885, delta=10)

    def test_ball_vy_is_negative_on_start(self):
        """Ball should move upward on start."""
        ball = BALL()
        self.assertLess(ball.vy, 0)

    def test_ball_bounces_off_left_wall(self):
        """Ball moving left past x=0 should flip vx to positive."""
        ball = BALL()
        ball.vx = -ball_speed
        ball.ball_rect.x = 0
        ball.update()
        self.assertGreater(ball.vx, 0)

    def test_ball_bounces_off_right_wall(self):
        """Ball moving right past screen edge should flip vx to negative."""
        ball = BALL()
        ball.vx = ball_speed
        ball.ball_rect.x = SCREEN_WIDTH - ball.ball_size
        ball.update()
        self.assertLess(ball.vx, 0)

    def test_ball_bounces_off_top_wall(self):
        """Ball moving up past y=0 should flip vy to positive."""
        ball = BALL()
        ball.vy = -ball_speed
        ball.ball_rect.y = 0
        ball.update()
        self.assertGreater(ball.vy, 0)

    def test_ball_destroyed_at_bottom(self):
        """Ball reaching the bottom of the screen should be marked for destruction."""
        ball = BALL()
        ball.vy = ball_speed
        ball.ball_rect.bottom = SCREEN_HEIGHT
        ball.update()
        self.assertTrue(ball.destroy)


class TestPaddle(unittest.TestCase):

    def test_paddle_rect_position(self):
        """Paddle rect should be at the given x, y position."""
        paddle = PADDLE(160, 10, 100, 600)
        self.assertEqual(paddle.paddle_rect.x, 100)
        self.assertEqual(paddle.paddle_rect.y, 600)

    def test_paddle_rect_dimensions(self):
        """Paddle rect should use the given width and height."""
        paddle = PADDLE(160, 10, 0, 0)
        self.assertEqual(paddle.paddle_rect.width, 160)
        self.assertEqual(paddle.paddle_rect.height, 10)

    def test_paddle_default_radius(self):
        """Paddle should initialize with the default border radius."""
        from breakout_main.settings import paddle_rad
        paddle = PADDLE(160, 10, 0, 0)
        self.assertEqual(paddle.rad, paddle_rad)


if __name__ == "__main__":
    unittest.main()
