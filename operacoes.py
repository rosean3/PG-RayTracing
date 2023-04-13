# normalize a vector, you can use numpy.linalg
import numpy

def normalize(v):
    norm = numpy.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def rotate_x(angle,point1, point2):
    angle = numpy.radians(angle)
    aux = point2 - point1
    aux = numpy.array([aux[0], aux[1] * numpy.cos(angle) - aux[2] * numpy.sin(angle),
                       aux[1] * numpy.sin(angle) + aux[2] * numpy.cos(angle)])
    point2 = aux + point1
    return point2


def rotate_y(angle,point1, point2):
    angle = numpy.radians(angle)
    aux = point2 - point1
    aux = numpy.array([aux[0] * numpy.cos(angle) + aux[2] * numpy.sin(angle), aux[1],
                       -aux[0] * numpy.sin(angle) + aux[2] * numpy.cos(angle)])
    point2 = aux + point1
    return point2

def rotate_z(angle,point1, point2):
    angle = numpy.radians(angle)
    aux = point2 - point1
    aux = numpy.array([aux[0] * numpy.cos(angle) - aux[1] * numpy.sin(angle),
                       aux[0] * numpy.sin(angle) + aux[1] * numpy.cos(angle), aux[2]])
    point2 = aux + point1
    return point2