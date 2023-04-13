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


def shade(O, objs, P, w,n,lights, e=10E-5):

    color = np.array(O.color)/255
    Cp = (float)(O.ka) * color

    for light in lights:
        l_normalized = normalize(light.position - P)
        r = reflect(l_normalized, n)
        new_P = P + e * l_normalized

        S = trace(objs, new_P, l_normalized)
        S.sort()

        t = 0
        if len(S) != 0:
            t, obj = S[0]

        if len(S) == 0 or (np.dot(l_normalized, light.position - new_P) < t):
            if np.dot(n, l_normalized) > 0:
                Cp += (O.kd * color) * (np.dot(n, l_normalized) * np.array(light.intensity)/255)

            if np.dot(w, r) > 0:
                Cp += O.ks * (np.dot(w, r) ** O.phong) * color

    return Cp

def reflect(l, n): return 2 * n * np.dot(l, n) - l


def cast(objects, ray_origin, ray_direction, ambient_light, light):
    color = (0,0,0)
    intersections = trace(objects, ray_origin, ray_direction)
    intersections.sort()

    if len(intersections) != 0:
        closest_obj = intersections[0][1]
        p = ray_origin + ray_direction * intersections[0][0]
        color = shade(closest_obj, objects, p, -1 * ray_direction, normalize(p), light)

    return color

def trace_image(camera, ambient_light, light, objects):
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
            aux = np.array(cast(objects, camera.focus, ray_direction,ambient_light, light))
            aux = aux/max(*aux, 1)
            img[i][j] = aux
    return img