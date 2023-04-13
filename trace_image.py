from objetos import *
from operacoes import *
import numpy as np


def trace(objects, ray_origin, ray_direction):
    '''
    Trace a ray in the scene to find the closest object
    '''
    intersections = []

    for object in objects:
        t = object.intersect(ray_origin, ray_direction)

        if t:
            intersections.append((t, object))

    return intersections


def shade(closest_obj, objects, p, v_vector, n_vector, ambient_light, lights, e=10E-5):
    '''
    Shade an intersection point in the scene
    '''
    final_color = closest_obj.ka * ambient_light.intensity

    if lights == None:
        return final_color

    for light in lights:
        l_vector = normalize(light.position - p)
        r_vector = reflect(l_vector, n_vector)
        new_P = p + e * l_vector

        intersections = trace(objects, new_P, l_vector)
        intersections.sort()

        t = 0
        if len(intersections) != 0:
            t = intersections[0][0]

        if len(intersections) == 0 or (np.dot(l_vector, light.position - new_P) < t):
            if np.dot(n_vector, l_vector) > 0: # ! caso dê negativo
                final_color += light.intensity * closest_obj.kd * closest_obj.color * (np.dot(n_vector, l_vector))

            if np.dot(v_vector, r_vector) > 0: # ! caso dê negativo
                final_color += light.intensity * closest_obj.ks * (np.dot(v_vector, r_vector) ** closest_obj.phong)

    return final_color


def cast(objects, lights, ray_origin, ray_direction, ambient_light):
    '''
    Cast a ray in the scene
    '''
    color = ambient_light.intensity
    intersections = trace(objects, ray_origin, ray_direction)
    intersections.sort()

    if len(intersections) != 0:
        closest_obj = intersections[0][1]
        p = ray_origin + (ray_direction * intersections[0][0])
        n_vector = closest_obj.get_normal(p)
        v_vector = -1 * ray_direction
        color = shade(closest_obj, objects, p, v_vector, n_vector, ambient_light, lights)

    return color

def trace_image(camera, ambient_light, lights, objects):
    Q = numpy.zeros((camera.v_res, camera.h_res, 3))
    img = numpy.zeros((camera.v_res, camera.h_res, 3))

    hx = 2 * camera.distance * numpy.tan(numpy.radians(camera.field_of_view)/2)
    hy = hx * camera.v_res / camera.h_res

    gx = hx/2
    gy = hy/2

    qx = (hx/(camera.h_res - 1)) * camera.b
    qy = (hy/(camera.v_res - 1)) * camera.v

    Q[0, 0] = camera.focus - camera.distance * camera.t - gx*camera.b + gy*camera.v

    for i in range(camera.v_res):
        for j in range(camera.h_res):
            Q[i, j] = Q[0, 0] + qx*j - qy*i
            ray_direction = normalize(Q[i, j] - camera.focus)
            lighting = np.array(cast(objects, lights, camera.focus, ray_direction, ambient_light))
            img[i][j] = normalize_lighting(lighting) # ! since we're always adding in shade, there's a possibility the value is higher than 1
    return img