from random import randrange

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from geometry import draw_origin, Cube


class Game:
    def __init__(self):
        sceen_scale = 4
        self.display = (200 * sceen_scale, 150 * sceen_scale)
        self.objs_buffer = []
        self.rotation = (0, 0, 0, 0)
        self.speed = [0, 0, 0]
        self.speedm = 3
        self.inizializate()

    def inizializate(self):
        pygame.init()
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 500.0)
        glTranslatef(0.0, 0.0, -300)
        glEnable(GL_DEPTH_TEST);

        for i in xrange(200):
            x = randrange(-100, 100, 1)
            y = randrange(-100, 100, 1)
            z = randrange(-100, 100, 1)
            print x, y, z
            self.objs_buffer.append(Cube(x, y, z))

    def loop(self):
        while True:
            try:
                self.process_events()
                self.update_game()
                self.update_sceen()
            except KeyboardInterrupt:
                self.byebye()

    def process_events(self):
        for event in pygame.event.get():
            esc = event.type == KEYDOWN and event.key == K_ESCAPE
            quit_game = event.type == pygame.QUIT

            if esc or quit_game:
                self.byebye()
            elif event.type == KEYDOWN and event.key == K_UP:
                self.speed[2] = self.speedm
            elif event.type == KEYUP and event.key == K_UP:
                self.speed[2] = 0

            elif event.type == KEYDOWN and event.key == K_DOWN:
                self.speed[2] = -self.speedm
            elif event.type == KEYUP and event.key == K_DOWN:
                self.speed[2] = 0

            elif event.type == KEYUP and event.key == K_LEFT:
                self.speed[0] = 0
            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.speed[0] = self.speedm

            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.speed[0] = -self.speedm
            elif event.type == KEYUP and event.key == K_RIGHT:
                self.speed[0] = 0

            elif event.type == MOUSEMOTION:
                self.rotate(event.rel)

    def rotate(self, rel):
        self.rotation = (1, 1 * rel[0], 1 * rel[1], 0)

    def move(self):
        glRotate(*self.rotation)
        glTranslatef(*self.speed)

    def update_game(self):
        self.move()

    def draw_scene(self):
        for obj in self.objs_buffer:
            # print obj
            obj.draw()

    def byebye(self):
        pygame.quit()

    def update_sceen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_origin()
        self.draw_scene()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    # done: fix Cube shape
    # todo: rotate translation vector
    # done: change speed and not position with movement keys
    # todo: detect colisions
    # todo: make rest of cubes to move
    # todo: upload code to git
    # todo: start in position and try to get to other position
    # todo: change the cubes for other shapes
    cubes = Game()
    cubes.loop()
