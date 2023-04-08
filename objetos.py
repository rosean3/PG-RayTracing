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
    
    def print_self(self):
        print("Center: ", self.center)
        print("Radius: ", self.radius)

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
    
    def print_self(self):
        print("Point: ", self.point)
        print("Normal: ", self.normal)

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
        self.a = numpy.array([int(x) for x in a])
        self.b = numpy.array([int(x) for x in b])
        self.c = numpy.array([int(x) for x in c])
    
    def print_self(self):
        print("A: ", self.a)
        print("B: ", self.b)
        print("C: ", self.c)
    
    def getTriangle(self):
        return (self.a, self.b, self.c)

    def intersect(self, ray_origin, ray_direction):
        e1 = self.b - self.a
        e2 = self.c - self.a
        p = numpy.cross(ray_direction, e2)
        a = e1.dot(p)
        if abs(a) < 1e-6:
            return None
        f = 1/a
        s = ray_origin - self.a
        u = f * s.dot(p)
        if u < 0 or u > 1:
            return None
        q = numpy.cross(s, e1)
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
    
    def generate_triangles(self):
        triangles = []
        for face in self.faces:
            triangle = Triangle(self.vertices[int(face[0])-1], self.vertices[int(face[1])-1], self.vertices[int(face[2])-1], self.color, self.kd, self.ks, self.ka, self.kr, self.kt, self.phong)
            triangles.append(triangle)
        return triangles
    
    def print_triangles(self):
        triangles = []
        for face in self.faces:
            triangle = Triangle(self.vertices[int(face[0])-1], self.vertices[int(face[1])-1], self.vertices[int(face[2])-1], self.color, self.kd, self.ks, self.ka, self.kr, self.kt, self.phong)
            triangles.append(triangle.getTriangle())
        return triangles

    def intersect(self, ray_origin, ray_direction):
        intersect = []
        for triangle in self.generateTriangles():
            if triangle.intersect(ray_origin, ray_direction) != None:
                intersect.append(triangle.intersect(ray_origin, ray_direction))
        
        if len(intersect) == 0:
            return None
        
        else:
            return min(intersect), 

    # def get_normal(self, point):
    #     return (self.b - self.a).cross(self.c - self.a).normalize()

    # def get_material(self):
    #     return self.material

class Camera:
    def __init__(self, height, width, d, up, focus, target, field_of_view = 90):
        self.height = height
        self.width = width
        self.d = d
        self.up = up
        self.focus = focus
        self.target = target
        self.field_of_view = field_of_view

class Light:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

class AmbientLight:
    def __init__(self, intensity):
        self.intensity = intensity