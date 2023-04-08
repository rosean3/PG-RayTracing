# ? fix this once we have a __init__.py file 
import sys
sys.path.append('/home/roseane/Documents/Faculdade/PG/Projeto/our_repo')

from objetos import *
from operacoes import *
from tools import *


objects = getInput('/home/roseane/Documents/Faculdade/PG/Projeto/our_repo/teste.txt')

# ! spheres
print("SPHERES:")
ray_origin = numpy.array((30.2,25,3))
ray_direction = normalize(numpy.array((-46.15,-46.01,-3)))

sphere1 = objects['sphere'][0]
sphere2 = objects['sphere'][1]
sphere1.print_self()
print(sphere1.intersect(ray_origin, ray_direction), '\n')
sphere2.print_self()
print(sphere2.intersect(ray_origin, ray_direction))

# ! planes
print("\nPLANES:")
ray_origin2 = numpy.array((-33.83208,-37.51405,30))
ray_direction2 = normalize(numpy.array((1, 0, 0)))

plano1 = objects['plane'][0] # red one
plano2 = objects['plane'][1] # blue one
plano1.print_self()
print(plano1.intersect(ray_origin2, ray_direction2), '\n')
plano2.print_self()
print(plano2.intersect(ray_origin2, ray_direction2))

# ! triangles
print("\nTRIANGLES:")
ray_origin3 = numpy.array((4,0.7,0.63533))
ray_direction3 = normalize(numpy.array((-7.15,0.1,-0.64)))

triangleMesh1 = objects['triangle'][0]
triangles = triangleMesh1.generate_triangles()
triangle1 = triangles[0]
triangle2 = triangles[1]
triangle1.print_self()
print(triangle1.intersect(ray_origin3, ray_direction3), '\n')
triangle2.print_self()
print(triangle2.intersect(ray_origin3, ray_direction3))