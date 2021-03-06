from window import Window
from constants import Constants
from snake import Snake
from cube import Cube
import pygame


def main():
    window = Window()
    clock = pygame.time.Clock()

    flag = True

    while flag:
        pygame.time.delay(Constants.FRAMERATE)
        clock.tick(10)

        window.draw_window()

        for cube in window.snake.cubes:
            window.draw_cube(cube)

        for cube in window.bot.cubes:
            window.draw_cube(cube)

        window.draw_cube(window.fruit)

        pygame.display.update()

        window.snake.move()
        window.bot.move(True, window.fruit.pos)

        positions = [cube.pos for cube in window.snake.cubes]

        for pos in positions:
            if positions.count(pos) > 1 or pos in [
                cube.pos for cube in window.bot.cubes
            ]:
                flag = False
                break

        if window.snake.check_collision(
            window.fruit
        ) or window.bot.check_collision(window.fruit):
            window.fruit.pos = window.generate_position()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
