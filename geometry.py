from OpenGL.GL import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

colors = (
    (1, 1, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)


def draw_origin():
    # x axis
    glBegin(GL_LINES)
    glVertex3fv((0, 0, 0))
    glVertex3fv((2, 0, 0))
    glEnd()
    # y axis
    glBegin(GL_LINES)
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 2, 0))
    glEnd()


def Cube2():
    glPushMatrix()
    glTranslatef(6, 0, 0)
    glBegin(GL_POLYGON)
    # glBegin(GL_POINTS)
    for edge in edges:
        for vertex in edge:
            # print(vertex, verticies[vertex])
            glVertex3fv(verticies[vertex])
            glColor3fv(colors[vertex])
    glEnd()
    glPopMatrix()


class Cube:
    def __init__(self, x, y, z, l=1):
        self.x = x
        self.y = y
        self.z = z
        self.l = l

    def draw2(self):

        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glBegin(GL_POLYGON)

        for edge in edges:
            for vertex in edge:
                glVertex3fv(verticies[vertex])
                glColor3fv(colors[vertex])
        glEnd()
        glPopMatrix()

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glScale(3, 3, 3)
        glBegin(GL_POLYGON)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, 0.5, -0.5)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-0.5, 0.5, -0.5)
        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glEnd()

        # Purple side - RIGHT
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glEnd()

        # Green side - LEFT
        glBegin(GL_POLYGON)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)
        glEnd()

        # Blue side - TOP
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glEnd()

        # Red side - BOTTOM
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(-0.5, -0.5, -0.5)
        glEnd()
        glPopMatrix()
