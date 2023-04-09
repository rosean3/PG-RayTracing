# ? fix this once we have a __init__.py file 
import sys
sys.path.append('/home/roseane/Documents/Faculdade/PG/Projeto/our_repo')
import matplotlib.pyplot as plt
import numpy

from objetos import *
from operacoes import *
from tools import *
from trace_image import *


objects, scene = getInput('/home/roseane/Documents/Faculdade/PG/Projeto/our_repo/teste.txt')

camera = scene['camera']
camera.print_self()

ambient_light = scene['ambient']

objects_list = [item for sublist in objects.values() for item in sublist]

image = trace_image(camera, ambient_light.intensity, objects_list)
plt.imsave("TESTEEE.png", image)