# ? fix this once we have a __init__.py file
import sys
import matplotlib.pyplot as plt
from tools import *
from trace_image import *

# ! teste 1 e 2
objects, scene = getInput(r'/home/roseane/Documents/Faculdade/PG/projeto-main/PG-RayTracing/teste1e2.txt')

camera = scene['camera']

camera.field_of_view = 45

ambient_light = scene['ambient']
objects_list = []
for obj in objects:
    if obj != 'triangle_mesh':
        objects_list.extend(objects[obj])

if "light" in scene:
    image = trace_image(camera, ambient_light, scene['light'], objects_list)

    # # imagem rotacionada
    camera.rotate(0, 0, -90, (0, 0, 0))
    image2 = trace_image(camera, ambient_light, scene['light'], objects_list)
    plt.imsave("imagem2.png", image2 )
else:
    image = trace_image(camera, ambient_light, None, objects_list)
plt.imsave("imagem.png", image )


# ! teste 3
objects, scene = getInput(r'/home/roseane/Documents/Faculdade/PG/projeto-main/PG-RayTracing/teste3.txt')
camera = scene['camera']
ambient_light = scene['ambient']
objects_list = []

for obj in objects:
    if obj != 'triangle_mesh':
        objects_list.extend(objects[obj])

# transladar esfera maior
if "sphere" in objects:
    objects['sphere'][0].translation((-4.31, -8.87, 7))

# transladar plano
if "plane" in objects:
    objects['plane'][0].translation((-4.31, -8.87, 7))


if "light" in scene:
    image3 = trace_image(camera, ambient_light, scene['light'], objects_list)
else:
    image3 = trace_image(camera, ambient_light, None, objects_list)

plt.imsave("imagem3.png", image3 )

# ! teste 4
objects, scene = getInput(r'/home/roseane/Documents/Faculdade/PG/projeto-main/PG-RayTracing/teste4.txt')
camera = scene['camera']
ambient_light = scene['ambient']
objects_list = []

for obj in objects:
    if obj != 'triangle_mesh':
        objects_list.extend(objects[obj])

# transladar esfera maior
if "sphere" in objects:
    objects['sphere'][0].translation((-4.31, -8.87, 7))

# transladar plano
if "plane" in objects:
    objects['plane'][0].translation((-4.31, -8.87, 7))


if "light" in scene:
    image4 = trace_image(camera, ambient_light, scene['light'], objects_list)
else:
    image4 = trace_image(camera, ambient_light, None, objects_list)

plt.imsave("imagem4.png", image4 )

# ! teste 5
objects, scene = getInput(r'/home/roseane/Documents/Faculdade/PG/projeto-main/PG-RayTracing/teste5.txt')
camera = scene['camera']
ambient_light = scene['ambient']
objects_list = []

for obj in objects:
    if obj != 'triangle_mesh':
        objects_list.extend(objects[obj])

# transladar esfera maior
if "sphere" in objects:
    objects['sphere'][0].translation((-4.31, -8.87, 7))

# transladar plano
if "plane" in objects:
    objects['plane'][0].translation((-4.31, -8.87, 7))


if "light" in scene:
    image5 = trace_image(camera, ambient_light, scene['light'], objects_list)
else:
    image5 = trace_image(camera, ambient_light, None, objects_list)

plt.imsave("imagem5.png", image5 )



