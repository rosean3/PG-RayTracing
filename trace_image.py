from objetos import *
from operacoes import *
import numpy as np


def trace(objects, ray_origin, ray_direction):
    intersections = []

    for obj in objects:
        t = obj.intersect(ray_origin, ray_direction)

        if t:
            intersections.append((t, obj))

    return intersections


def shade(closest_obj, objects, p, view_vector, normal_vector, ambient_light, lights, e=10E-5):
    final_color = closest_obj.ka * (closest_obj.color/255) * ambient_light.intensity

    for light in lights:
        l_vector = normalize(light.position - p)
        r = reflect(l_vector, normal_vector)
        new_P = p + e * l_vector

        intersections = trace(objects, new_P, l_vector)
        intersections.sort()

        t = 0
        if len(intersections) != 0:
            t, obj = intersections[0]

        if len(intersections) == 0 or (np.dot(l_vector, light.position - new_P) < t):
            if np.dot(normal_vector, l_vector) > 0:
                final_color += (closest_obj.kd * (closest_obj.color/255)) * (np.dot(normal_vector, l_vector) * light.intensity)

            if np.dot(view_vector, r) > 0:
                final_color += closest_obj.ks * (np.dot(view_vector, r) ** closest_obj.phong) * light.intensity

    return final_color


def cast(objects, lights, ray_origin, ray_direction, ambient_light):
    color = (0,0,0)
    intersections = trace(objects, ray_origin, ray_direction)
    intersections.sort()

    if len(intersections) != 0:
        closest_obj = intersections[0][1]
        p = ray_origin + (ray_direction * intersections[0][0])
        normal_vector = closest_obj.get_normal(p)
        view_vector = -1 * ray_direction
        color = shade(closest_obj, objects, p, view_vector, closest_obj.get_normal(p), ambient_light, lights)

    return color

def reflect(l, n): return 2 * n * np.dot(l, n) - l

def trace_image(camera, ambient_light, lights, objects):
    print("camera: ")
    camera.print_self()
    t = normalize([a - b for a, b in zip(camera.target,camera.focus)]) # ! n: vetor normal (normalizado)
    t = t * -1
    b = normalize(numpy.cross(camera.up, t)) # ! b: vetor horizontal (normalizado)
    v = numpy.cross(t, b) # ! v: vetor vertical (normalizado)


    # Fred's trick
    Q = numpy.zeros((camera.v_res, camera.h_res, 3)) # ! matriz de pontos de projeção
    img = numpy.zeros((camera.v_res, camera.h_res, 3)) # ! matriz de pixels

    hx = 2 * camera.distance * numpy.tan(numpy.radians(camera.field_of_view)/2)
    hy = hx * camera.v_res / camera.h_res

    gx = hx/2
    gy = hy/2

    qx = (hx/(camera.h_res - 1)) * b
    qy = (hy/(camera.v_res - 1)) * v

    Q[0, 0] = camera.focus - camera.distance * t - gx*b + gy*v

    for i in range(camera.v_res):
        for j in range(camera.h_res):
            Q[i, j] = Q[0, 0] + qx*j - qy*i
            ray_direction = normalize(Q[i, j] - camera.focus)
            aux = np.array(cast(objects, lights, camera.focus, ray_direction, ambient_light))
            aux = aux/max(*aux, 1)
            img[i][j] = aux
    return img