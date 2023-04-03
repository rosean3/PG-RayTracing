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
        

    # def intersect(self, ray):
    #     oc = ray.origin - self.center
    #     a = ray.direction.dot(ray.direction)
    #     b = 2.0 * oc.dot(ray.direction)
    #     c = oc.dot(oc) - self.radius * self.radius
    #     discriminant = b * b - 4 * a * c
    #     if discriminant > 0:
    #         temp = (-b - math.sqrt(discriminant)) / (2.0 * a)
    #         if temp < 0:
    #             temp = (-b + math.sqrt(discriminant)) / (2.0 * a)
    #         if temp > 0:
    #             return temp
    #     return None

    # def get_normal(self, point):
    #     return (point - self.center).normalize()

    # def get_material(self):
    #     return self.material

class Plane(Object):
    def __init__(self, point, normal, color, kd, ks, ka, kr, kt, phong):
        super().__init__(color, kd, ks, ka, kr, kt, phong)
        self.point = point
        self.normal = normal

    # def intersect(self, ray):
    #     denom = self.normal.dot(ray.direction)
    #     if abs(denom) > 0.0001:
    #         d = self.point - ray.origin
    #         t = d.dot(self.normal) / denom
    #         if t > 0:
    #             return t
    #     return None

    # def get_normal(self, point):
    #     return self.normal

    # def get_material(self):
    #     return self.material

class Triangle(Object):
    def __init__(self, a, b, c, color, kd, ks, ka, kr, kt, phong):
        super().__init__(color, kd, ks, ka, kr, kt, phong)
        self.a = [int(x) for x in a]
        self.b = [int(x) for x in a]
        self.c = [int(x) for x in a]

    
    def getTriangle(self):
        return (self.a, self.b, self.c)

    # def intersect(self, ray):
    #     e1 = self.b - self.a
    #     e2 = self.c - self.a
    #     p = ray.direction.cross(e2)
    #     a = e1.dot(p)
    #     if abs(a) < 0.0001:
    #         return None
    #     f = 1.0 / a
    #     s = ray.origin - self.a
    #     u = f * s.dot(p)
    #     if u < 0.0 or u > 1.0:
    #         return None
    #     q = s.cross(e1)
    #     v = f * ray.direction.dot(q)
    #     if v < 0.0 or u + v > 1.0:
    #         return None
    #     t = f * e2.dot(q)
    #     if t > 0.0001:
    #         return t
    #     else:
    #         return None

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

    # def intersect(self, ray):
    #     t = None
    #     for face in self.faces:
    #         triangle = Triangle(self.vertices[face[0]], self.vertices[face[1]], self.vertices[face[2]])
    #         t = triangle.intersect(ray)
    #         if t is not None:
    #             return t
    #     return None

    # def get_normal(self, point):
    #     return (self.b - self.a).cross(self.c - self.a).normalize()

    # def get_material(self):
    #     return self.material