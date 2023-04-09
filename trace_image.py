from objetos import *
from operacoes import *

def trace(objects, ray_origin, ray_direction):
    intersections = []

    for obj in objects:
        t = obj.intersect(ray_origin, ray_direction)

        if t:
            intersections.append((t, obj))

    return intersections

def cast(objects, ray_origin, ray_direction, ambient_light):
    color = ambient_light
    intersections = trace(objects, ray_origin, ray_direction)

    intersections.sort()
    if len(intersections) != 0:
        closest_obj = intersections[0][1]
        color = closest_obj.color

    return color

def trace_image(camera, ambient_light, objects):
    print("camera: ")
    camera.print_self()
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
            ray_direction = normalize(Q[i, j] - camera.focus)
            img[i, j] = cast(objects, camera.focus, ray_direction, ambient_light)

    return img / 255