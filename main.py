from OpenGL.GLU import *
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
    z=0
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()



        glClearColor(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor(0, 0, 1)
        glBegin(GL_QUADS)
        glVertex3f(-1, 1, -4)
        glVertex3f(-1, 1, 4)
        glVertex3f(-1, -1, 4)
        glVertex3f(-1, -1, -4)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(1, 1, -4)
        glVertex3f(1, 1, 4)
        glVertex3f(1, -1, 4)
        glVertex3f(1, -1, -4)
        glEnd()

        glPushMatrix()
        glRotatef(-60, 1, 0, 1)
        glRotatef(33, 0, 0, 1)
        glTranslatef(1, 0, -4)

        glPushMatrix()
        #glRotatef(theta, 0, 1, 0)


        position = [0, 0, z, 1]
        color_d=[1, 0, 0, 1]
        glLightfv(GL_LIGHT0, GL_POSITION, position)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, color_d)

        glTranslatef(0, z+1, 1)
        glScalef(0.2, 0.2, 0.2)
        glColor3f(1, 1, 1)
        glutSolidSphere(0.275, 250, 250)

        glPopMatrix()


        glTranslatef(0, z, 0)
        color = [1, 1, 1, 1]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        glutSolidSphere(0.275, 250, 250)

        glPopMatrix()

        glutSwapBuffers()
        theta+=15
        if z<6:
            z+=0.1
        else:
            z-=5
        time.sleep(0.1)



    return
main()