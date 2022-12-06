from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import sys
import pygame as pg
import time
from math import *
from numpy import *

PI = 3.141592653




def init():


    glClearColor (0.3, 0.3, 0.3, 0.0)

    glEnable(GL_LIGHTING)

    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)

    glEnable(GL_NORMALIZE)


def reshape(width, height):


    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.2, 1.2, -1.2, 1.2, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global light_sample
    material_diffuse = [1.0, 1.0, 1.0, 1.0]
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, material_diffuse)

    if (light_sample == 1):


        light0_diffuse = [0.4, 0.7, 0.2]
        light0_direction = [0.0, 0.0, 1.0, 0.0]
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
        glLightfv(GL_LIGHT0, GL_POSITION, light0_direction)

    if (light_sample == 2):


        light1_diffuse = [0.4, 0.7, 0.2]
        light1_position = [0.0, 0.0, 1.0, 1.0]
        glEnable(GL_LIGHT1)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
        glLightfv(GL_LIGHT1, GL_POSITION, light1_position)

    if (light_sample == 3):


        light2_diffuse = [0.4, 0.7, 0.2]
        light2_position = [0.0, 0.0, 1.0, 1.0]
        glEnable(GL_LIGHT2)
        glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_diffuse)
        glLightfv(GL_LIGHT2, GL_POSITION, light2_position)
        glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.2)
        glLightf(GL_LIGHT2, GL_QUADRATIC_ATTENUATION, 0.4)

    if (light_sample == 4):


        light3_diffuse = [0.4, 0.7, 0.2]
        light3_position = [0.0, 0.0, 1.0, 1.0]
        light3_spot_direction = [0.0, 0.0, -1.0]
        glEnable(GL_LIGHT3)
        glLightfv(GL_LIGHT3, GL_DIFFUSE, light3_diffuse)
        glLightfv(GL_LIGHT3, GL_POSITION, light3_position)
        glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 30)
        glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, light3_spot_direction)

    if (light_sample == 5):

        light4_diffuse = [0.4, 0.7, 0.2]
        light4_position = [0.0, 0.0, 1.0, 1.0]
        light4_spot_direction = [0.0, 0.0, -1.0]
        glEnable(GL_LIGHT4)
        glLightfv(GL_LIGHT4, GL_DIFFUSE, light4_diffuse)
        glLightfv(GL_LIGHT4, GL_POSITION, light4_position)
        glLightf(GL_LIGHT4, GL_SPOT_CUTOFF, 30)
        glLightfv(GL_LIGHT4, GL_SPOT_DIRECTION, light4_spot_direction)
        glLightf(GL_LIGHT4, GL_SPOT_EXPONENT, 30.0)

    if (light_sample == 6):

        light5_diffuse = [1.0, 0.0, 0.0]
        light5_position = [0.5 * cos(0.0), 0.5 * sin(0.0), 1.0, 1.0]
        glEnable(GL_LIGHT5)
        glLightfv(GL_LIGHT5, GL_DIFFUSE, light5_diffuse)
        glLightfv(GL_LIGHT5, GL_POSITION, light5_position)
        glLightf(GL_LIGHT5, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(GL_LIGHT5, GL_LINEAR_ATTENUATION, 0.4)
        glLightf(GL_LIGHT5, GL_QUADRATIC_ATTENUATION, 0.8)
        light6_diffuse = [0.0, 1.0, 0.0]
        light6_position = [0.5 * cos(2 * PI / 3), 0.5 * sin(2 * PI / 3), 1.0, 1.0]
        glEnable(GL_LIGHT6)
        glLightfv(GL_LIGHT6, GL_DIFFUSE, light6_diffuse)
        glLightfv(GL_LIGHT6, GL_POSITION, light6_position)
        glLightf(GL_LIGHT6, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(GL_LIGHT6, GL_LINEAR_ATTENUATION, 0.4)
        glLightf(GL_LIGHT6, GL_QUADRATIC_ATTENUATION, 0.8)
        light7_diffuse= [0.0, 0.0, 1.0]
        light7_position = [0.5 * cos(4 * PI / 3), 0.5 * sin(4 * PI / 3), 1.0, 1.0]
        glEnable(GL_LIGHT7)
        glLightfv(GL_LIGHT7, GL_DIFFUSE, light7_diffuse)
        glLightfv(GL_LIGHT7, GL_POSITION, light7_position)
        glLightf(GL_LIGHT7, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(GL_LIGHT7, GL_LINEAR_ATTENUATION, 0.4)
        glLightf(GL_LIGHT7, GL_QUADRATIC_ATTENUATION, 0.8)


    
    glutSolidSphere(1, 250, 250)

    glDisable(GL_LIGHT0)
    glDisable(GL_LIGHT1)
    glDisable(GL_LIGHT2)
    glDisable(GL_LIGHT3)
    glDisable(GL_LIGHT4)
    glDisable(GL_LIGHT5)
    glDisable(GL_LIGHT6)
    glDisable(GL_LIGHT7)

    glutSwapBuffers()


def keyboard_function(key, x, y):
    global light_sample
    if (key == GLUT_KEY_F1):
        light_sample = 1
    if (key == GLUT_KEY_F2):
        light_sample = 2
    if (key == GLUT_KEY_F3):
        light_sample = 3
    if (key == GLUT_KEY_F4):
        light_sample = 4
    if (key == GLUT_KEY_F5):
        light_sample = 5
    if (key == GLUT_KEY_F6):
        light_sample = 6
    glutPostRedisplay()

light_sample = 6
def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(50, 100)
    glutInitWindowSize(500, 500)
    glutCreateWindow("4.4. Пример установки источников света в OpenGL. (с) compgraphics.info")
    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(keyboard_function)
    glutMainLoop()
main()
