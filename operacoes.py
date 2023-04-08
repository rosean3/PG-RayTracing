# normalize a vector, you can use numpy.linalg
import numpy

def normalize(v):
    norm = numpy.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm