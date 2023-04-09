# ? fix this once we have a __init__.py file 
import sys
sys.path.append('/home/roseane/Documents/Faculdade/PG/Projeto/our_repo')
import matplotlib.pyplot as plt
import numpy

from objetos import *
from operacoes import *
from tools import *

def trace_image(camera, ambient_light):
    t = normalize(camera.target - camera.focus) # ! n: vetor normal (normalizado)
    b = normalize(numpy.cross(camera.up, t)) # ! b: vetor horizontal (normalizado)
    v = numpy.cross(t, b) # ! v: vetor vertical (normalizado)
    t = t*-1

    # Fred's trick
    Q = numpy.zeros((camera.v_res, camera.h_res, 3)) # ! matriz de pontos de projeção
    img = numpy.zeros((camera.v_res, camera.h_res, 3)) # ! matriz de pixels

    hx = 2 * camera.distance * numpy.tan(numpy.radians(camera.field_of_view)/2)
    hy = hx * camera.v_res / camera.h_res

    gx = hx/2
    gy = hy/2

    qx = (hx/(camera.h_res - 1)) * b
    qy = (hy/(camera.v_res - 1)) * v

    Q[0, 0] = camera.focus - camera.distance*t - gx*b + gy*v

    for i in range(camera.v_res):
        for j in range(camera.h_res):
            Q[i, j] = Q[0, 0] + qx*j - qy*i
            # ray_D = normalize(Q[i, j] - E)
            # img[i, j] = cast(objs, E, ray_D, background_color)
            img[i, j] = ambient_light.intensity

    return img / 255


objects, scene = getInput('/home/roseane/Documents/Faculdade/PG/Projeto/our_repo/teste.txt')

camera = scene['camera']
camera.print_self()

ambient_light = scene['ambient']

image = trace_image(camera, ambient_light)
plt.imsave("testing_trace.png", image)
