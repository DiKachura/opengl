"""from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import sys
import pygame as pg
import time
from math import *
from numpy import *


def main():

    pg.init()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GL_DEPTH_BUFFER_BIT)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(450, 5)
    glutCreateWindow("Light")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-0.1, 0.1, -0.1, 0.1, 0.2, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    theta = 0
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        for x in arange(-15 + 1, 15 - 1, 0.5):

            glClearColor(0, 0, 0, 0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            z = cos(x)
            glPushMatrix()
            glRotatef(-60, 1, 0, 0)
            glRotatef(33, 0, 0, 1)
            glTranslatef(2, 3, -2)
            glPushMatrix()
            glRotatef(theta, 0, 0, 0)
            glTranslatef(0, 0, z)
            glTranslatef(0, 0, z)

            position = [0, 0, 1, 1]
            glLightfv(GL_LIGHT0, GL_POSITION, position)

            glTranslatef(0, 0, 1)
            glScalef(0.2, 0.2, 0.2)
            glColor3f(1, 1, 1)
            glutSolidSphere(0.275, 250, 250)
            glPopMatrix()

            glColor3f(0, 1, 0)
            glutSolidTorus(0.275, 0.85, 250, 250)

            glPopMatrix()

            glutSwapBuffers()
            theta+=15



    return
main()"""

import pygame
import math
from pygame.locals import *
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import pygame
def display():
    global xRot, yRot
    glClearColor(.7, .70, .70, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0, 1, 0)
    glPushMatrix()
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 0.0, 1.0)
    color = [0.5, 0.2, 0.0, 1.0]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    glTranslatef(0.5, -0.5, 0)
    glutSolidSphere(1.5, 60, 60)# тело
    glTranslatef(0, 1.7, 0)
    glutSolidSphere(1.25, 60, 60)# голова

    #уши
    color = [0., 0., 0.0, 1.0]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    glTranslatef(1, 1, 0)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(-2, 0, 0)
    glutSolidSphere(0.4, 60, 60)

    #лапы
    glTranslatef(-0.5, -2, 0)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(3, 0, 0)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(-1, -2, 0)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(-1, 0, 0)
    glutSolidSphere(0.4, 60, 60)

    #морда
    glTranslatef(0.5, 3.5, 0.8)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(0.3, 0, 0)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(0.2, 0, 0)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(-0.2, 0, 0)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(-0.2, 0, 0)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(-0.2, 0, 0)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(-0.2, 0, 0)
    glutSolidSphere(0.4, 60, 60)

    glTranslatef(-0.2, 0, 0)
    glutSolidSphere(0.4, 60, 60)

    #глаза
    color = [1, 1, 1, 1.0]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    glTranslatef(0, 0, 0.25)
    glutSolidSphere(0.2, 60, 60)

    glTranslatef(1, 0, 0)
    glutSolidSphere(0.2, 60, 60)

    #зрачки
    color = [0., 0., 0.0, 1.0]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    glTranslatef(0, 0, 0.25)
    glutSolidSphere(0.1, 60, 60)

    glTranslatef(-1, 0, 0)
    glutSolidSphere(0.1, 60, 60)

    #нос
    glTranslatef(0.5, -0.5, 0)
    glutSolidSphere(0.3, 60, 60)

    #рот
    glTranslatef(0, -0.5, 0)
    glutSolidSphere(0.1, 60, 60)

    glPopMatrix()
    glutSwapBuffers()
    return
def SpecialKeys(key, x, y):
    global xRot, yRot
    if (key == GLUT_KEY_UP):
        xRot -= 5.0
    if (key == GLUT_KEY_DOWN):
        xRot += 5.0
    if (key == GLUT_KEY_LEFT):
        yRot -= 5.0
    if (key == GLUT_KEY_RIGHT):
        yRot += 5.0
    glutPostRedisplay()
xRot = 0.0
yRot = 0.0
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 700)
    glutCreateWindow(b'sphere')
    glClearColor(0.2,0.3,0.5,0.5)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    lightZeroColor = [0.8,1.0,0.8,1.0]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glutSpecialFunc(SpecialKeys)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()
    return
main()