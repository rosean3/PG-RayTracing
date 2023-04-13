# ? fix this once we have a __init__.py file 
import sys
sys.path.append('/home/roseane/Documents/Faculdade/PG/Projeto/our_repo')
import matplotlib.pyplot as plt
import numpy

from objetos import *
from operacoes import *
from tools import *
from trace_image import *


objects, scene = getInput(r'/home/roseane/Documents/Faculdade/PG/Projeto/our_repo/teste.txt')

camera = scene['camera']

ambient_light = scene['ambient']
objects_list = []
for obj in objects:
    objects_list.extend(objects[obj])


#translada um objeto


if "light" in scene:
    image = trace_image(camera, ambient_light, scene['light'], objects_list)

    #objects_list[0].translation((40, 0, 0))
    #image2 = trace_image(camera, ambient_light.intensity, scene['light'], objects_list)

    #camera.rotate_y(30)
    #image3 = trace_image(camera, ambient_light.intensity, scene['light'], objects_list)


else:
    image = trace_image(camera, ambient_light, None, objects_list)

plt.imsave("TESTEEE.png", image )