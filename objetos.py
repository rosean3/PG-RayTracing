import math
import numpy

class Object:
    def __init__(self, color, kd, ks, ka, kr, kt, phong):
        self.color = color
        self.kd = kd
        self.ks = ks
        self.ka = ka
        self.kr = kr
        self.kt = kt
        self.phong = phong
    


class Sphere(Object):
    def __init__(self, center, radius, color, kd, ks, ka, kr, kt, phong):
        super().__init__(color, kd, ks, ka, kr, kt, phong)
        self.center = center
        self.radius = radius
        

    def intersect(self, ray_origin, ray_direction):
        I = self.center - ray_origin
        Tca = numpy.dot(I, ray_direction)
        D_sqrt = numpy.dot(I, I) - (Tca ** 2)

        if D_sqrt > (self.radius ** 2):
            return None
        else:
            Thc = ((self.radius ** 2) - D_sqrt) ** 0.5
            t0, t1 = Tca - Thc, Tca + Thc

            if t0 > t1:
                t0, t1 = t1, t0
            elif t0 < 0:
                if t1 < 0:
                    return None
                else:
                    return t1

            return t0

class Plane(Object):
    def __init__(self, point, normal, color, kd, ks, ka, kr, kt, phong):
        super().__init__(color, kd, ks, ka, kr, kt, phong)
        self.point = point
        self.normal = normal

    def intersect(self, ray_origin, ray_direction):
        denom = numpy.dot(self.normal, ray_direction)
        if abs(denom) > 1e-6:
            t = numpy.dot(self.normal, self.point - ray_origin)/ denom
            if t < 0:
                return None
            if t >= 0:
                return t
        return None

class Triangle(Object):
    def __init__(self, a, b, c, color, kd, ks, ka, kr, kt, phong):
        super().__init__(color, kd, ks, ka, kr, kt, phong)
        self.a = [int(x) for x in a]
        self.b = [int(x) for x in b]
        self.c = [int(x) for x in c]

    
    def getTriangle(self):
        return (self.a, self.b, self.c)

    def intersect(self, ray_origin, ray_direction):
        e1 = self.b - self.a
        e2 = self.c - self.a
        p = ray_direction.cross(e2)
        a = e1.dot(p)
        if abs(a) < 1e-6:
            return None
        f = 1/a
        s = ray_origin - self.a
        u = f * s.dot(p)
        if u < 0 or u > 1:
            return None
        q = s.cross(e1)
        v = f * ray_direction.dot(q)
        if v < 0 or u + v > 1:
            return None
        t = f * e2.dot(q)
        if t > 1e-6:
            return t
        else:
            return None

    # def get_normal(self, point):
    #     return (self.b - self.a).cross(self.c - self.a).normalize()

    # def get_material(self):
    #     return self.material

class TriangleMesh(Object):
    def __init__(self, faces, vertices, color, kd, ks, ka, kr, kt, phong):
        super().__init__(color, kd, ks, ka, kr, kt, phong)
        self.vertices = vertices
        self.faces = faces
    
    def generateTriangles(self):
        triangles = []
        for face in self.faces:
            triangle = Triangle(self.vertices[int(face[0])-1], self.vertices[int(face[1])-1], self.vertices[int(face[2])-1], self.color, self.kd, self.ks, self.ka, self.kr, self.kt, self.phong)
            triangles.append(triangle)
        return triangles
    
    def printTriangles(self):
        triangles = []
        for face in self.faces:
            triangle = Triangle(self.vertices[int(face[0])-1], self.vertices[int(face[1])-1], self.vertices[int(face[2])-1], self.color, self.kd, self.ks, self.ka, self.kr, self.kt, self.phong)
            triangles.append(triangle.getTriangle())
        return triangles

    def intersect(self, ray_origin, ray_direction):
        for triangle in self.generateTriangles():
            if triangle.intersect(ray_origin, ray_direction) != None:
                return triangle.intersect(ray_origin, ray_direction)

    # def get_normal(self, point):
    #     return (self.b - self.a).cross(self.c - self.a).normalize()

    # def get_material(self):
    #     return self.material

class Camera:
    def __init__(self, height, width, d, up, focus, M):
        self.height = height
        self.width = width
        self.d = d
        self.up = up
        self.focus = focus
        self.M = M

class Light:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

class AmbientLight:
    def __init__(self, intensity):
        self.intensity = intensity