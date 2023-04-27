# normalize a vector, you can use numpy.linalg
import numpy

def normalize(v):
    '''
    Normalize a vector
    '''
    norm = numpy.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

def normalize_lighting(color):
    '''
    Normalize the lighting
    '''
    return color/max(*color, 1)

def reflect(l, n):
    '''
    Reflect a vector l in a normal n
    '''
    return 2 * n * numpy.dot(l, n) - l

def rotate_x(angle, point,center):
    angle = numpy.radians(angle)
    aux = center - point
    aux = numpy.array([aux[0], aux[1] * numpy.cos(angle) - aux[2] * numpy.sin(angle),
                       aux[1] * numpy.sin(angle) + aux[2] * numpy.cos(angle)])
    center = aux + point
    return center


def rotate_y(angle,point, center):
    angle = numpy.radians(angle)
    aux = center - point
    aux = numpy.array([aux[0] * numpy.cos(angle) + aux[2] * numpy.sin(angle), aux[1],
                       -aux[0] * numpy.sin(angle) + aux[2] * numpy.cos(angle)])
    center = aux + point
    return center

def rotate_z(angle,point, center):
    angle = numpy.radians(angle)
    aux = center - point
    aux = numpy.array([aux[0] * numpy.cos(angle) - aux[1] * numpy.sin(angle),
                       aux[0] * numpy.sin(angle) + aux[1] * numpy.cos(angle), aux[2]])
    center = aux + point
    return center