# ? fix this once we have a __init__.py file
import sys
import matplotlib.pyplot as plt
from tools import *
from trace_image import *


objects, scene = getInput(r'C:\Users\arthu\OneDrive\Documentos\GitHub\PG-RayTracing\teste.txt')

camera = scene['camera']

ambient_light = scene['ambient']
objects_list = []
for obj in objects:
    if obj != 'triangle_mesh':
        objects_list.extend(objects[obj])

#translada objetos
if "sphere" in objects:
    objects['sphere'][0].translation((-4.31, -8.87, 7))


if "light" in scene:

    #imagem original
    image = trace_image(camera, ambient_light, scene['light'], objects_list)

    # rotaciona camera
    camera.rotate(0, 0, -90, (0, 0, 0))

    # imagem rotacionada
    image2 = trace_image(camera, ambient_light, scene['light'], objects_list)



else:
    image = trace_image(camera, ambient_light, None, objects_list)

plt.imsave("imagem.png", image )