import pygame


class Ball:
    __ball_image = pygame.image.load("intro_ball.gif")
    __ball_image_width = __ball_image.get_width()
    __ball_image_height = __ball_image.get_height()
    __ball_image_half_width = __ball_image.get_width() / 2
    __ball_image_half_height = __ball_image.get_height() / 2
    bounces_by_balls = 0

    @staticmethod
    def get_bounces_text():
        return "Total bounces {}".format(Ball.bounces_by_balls)

    def __init__(self, x, y, speed_x, speed_y, ball_size_factor=0.9):
        self.ball_x = x
        self.ball_y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.angle = 10
        self.spin_speed = 5
        self.ball_size_factor = ball_size_factor
        self.actual_ball_size = Ball.__ball_image_width * (1 - self.ball_size_factor)
        self.actual_ball_size_half = self.actual_ball_size // 2

    def update_model(self, world_width, world_height):

        # velocity = initial velocity + acceleration*time
        if self.speed_y != 0:
            acc = 9.81 if self.speed_y > 0 else 9.81
            self.speed_y = self.speed_y + acc * 0.1

        self.ball_x = self.ball_x + self.speed_x
        self.ball_y = self.ball_y + self.speed_y



        if self.speed_y != 0 and self.ball_y > world_height - self.actual_ball_size_half:
            # bottom wall
            Ball.bounces_by_balls += 1

            self.speed_y = -self.speed_y * self.ball_size_factor
            if abs(self.speed_y) < 1:
                self.speed_y = 0

            self.spin_speed = 5 if self.speed_x < 0 and self.speed_y >= 0 else -5
            self.ball_y = world_height - self.actual_ball_size_half

        if self.ball_x < self.actual_ball_size_half:
            # left wall
            self.speed_x = -self.speed_x * 0.8

            self.spin_speed = 5 if self.speed_x < 0 and self.speed_y <= 0 else -5
            self.ball_x = self.actual_ball_size_half
            Ball.bounces_by_balls += 1

        if self.ball_x > world_width - self.actual_ball_size_half:
            # right wall
            self.speed_x = -self.speed_x * 0.8
            self.spin_speed = 5 if self.speed_x < 0 and self.speed_y >= 0 else -5
            self.ball_x = world_width - self.actual_ball_size_half
            Ball.bounces_by_balls += 1

        if self.ball_y < self.actual_ball_size_half:
            # top wall
            self.spin_speed = 5 if self.speed_x > 0 and self.speed_y < 0 else -5
            self.speed_y = 1
            self.ball_y = self.actual_ball_size_half
            Ball.bounces_by_balls += 1
            pass

        self.angle += self.spin_speed


    def draw(self, screen):
        scaled_ball = pygame.transform.scale(Ball.__ball_image, (self.actual_ball_size, self.actual_ball_size))
        # scaled_ball = pygame.transform.scale(Ball.__ball_image, (Ball.__ball_image_width * (1 - self.ball_size_factor),
        #                                                          Ball.__ball_image_height * (1 - self.ball_size_factor)))
        rotated_image = pygame.transform.rotate(scaled_ball, self.angle)
        ball_rect = rotated_image.get_rect(center=(self.ball_x, self.ball_y))
        screen.blit(rotated_image, ball_rect)
