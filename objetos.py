from operacoes import *
class Object:
    def __init__(self, color, kd, ks, ka, kr, kt, phong):
        self.color = numpy.array([float(c) for c in color])/255
        self.kd = float(kd)
        self.ks = float(ks)
        self.ka = float(ka)
        self.kr = float(kr)
        self.kt = float(kt)
        self.phong = float(phong)
    


class Sphere(Object):
    def __init__(self, center, radius, color, kd, ks, ka, kr, kt, phong):
        super().__init__(color, kd, ks, ka, kr, kt, phong)
        self.center = numpy.array([float(c) for c in center])
        self.radius = float(radius)
    
    def print_self(self):
        print("Center: ", self.center)
        print("Radius: ", self.radius)

    def intersect(self, ray_origin, ray_direction):
        I = [a - b for a, b in zip(self.center, ray_origin)]
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

    def translation(self, vector):
        self.center = [v1 + v2 for v1, v2  in zip(self.center, vector)]

    def rotate(self, x=0, y=0, z=0, point = (0,0,0)):
        self.center = rotate_x(self.center, x, point)
        self.center = rotate_y(self.center, y, point)
        self.center = rotate_z(self.center, z, point)

    
    def get_normal(self, p):
        return normalize(p - self.center)


class Plane(Object):
    def __init__(self, point, normal, color, kd, ks, ka, kr, kt, phong):
        super().__init__(color, kd, ks, ka, kr, kt, phong)
        self.point = numpy.array([float(p) for p in point])
        self.normal = numpy.array([float(n) for n in normal])
    
    def print_self(self):
        print("Point: ", self.point)
        print("Normal: ", self.normal)

    def intersect(self, ray_origin, ray_direction):
        denom = numpy.dot(self.normal, ray_direction)
        if abs(denom) > 1e-6:
            t = numpy.dot(self.normal, [a - b for a,b in zip(self.point, ray_origin)])/ denom
            if t < 0:
                return None
            if t >= 0:
                return t
        return None

    def translation(self, vector):
        self.point = [v1 + v2 for v1, v2 in zip(self.point, vector)]

    def rotate(self, x=0, y=0, z=0, point = (0,0,0)):
        self.point = rotate_x(x, point, self.point)
        self.point = rotate_y(y, point, self.point)
        self.point = rotate_z(z, point, self.point)
        self.normal = rotate_x(x, point, self.normal)
        self.normal = rotate_y(y, point, self.normal)
        self.normal = rotate_z(z, point, self.normal)

    def get_normal(self, p):
        return normalize(self.normal)

class Triangle(Object):
    def __init__(self, a, b, c, color, kd, ks, ka, kr, kt, phong):
        super().__init__(color, kd, ks, ka, kr, kt, phong)
        self.a = numpy.array([float(x) for x in a])
        self.b = numpy.array([float(x) for x in b])
        self.c = numpy.array([float(x) for x in c])
    
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

    def translation(self, vector):
        self.a = [v1 + v2 for v1, v2 in zip(self.a, vector)]
        self.b = [v1 + v2 for v1, v2 in zip(self.b, vector)]
        self.c = [v1 + v2 for v1, v2 in zip(self.c, vector)]
    
    def get_normal(self, p):
        return normalize(numpy.cross(self.b - self.a, self.c - self.a))

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
        for triangle in self.generate_triangles():
            if triangle.intersect(ray_origin, ray_direction) != None:
                intersect.append(triangle.intersect(ray_origin, ray_direction))
        
        if len(intersect) == 0:
            return None
        
        else:
            return min(intersect),

    def translation(self, vector):
        for i in range(len(self.vertices)):
            self.vertices[i] = [v1 + v2 for v1, v2 in zip(self.vertices[i], vector)]

    def rotate(self, x = 0, y = 0, z = 0, point = (0, 0, 0)):
        for i in range(len(self.vertices)):
            self.vertices[i] = rotate_x(self.vertices[i], x, point)
            self.vertices[i] = rotate_y(self.vertices[i], y, point)
            self.vertices[i] = rotate_z(self.vertices[i], z, point)

class Camera:
    def __init__(self, h_res, v_res, distance, up, focus, target, field_of_view = 90):
        self.h_res = int(h_res)
        self.v_res = int(v_res)
        self.distance = float(distance)
        self.up = numpy.array([float(u) for u in up])
        self.focus = numpy.array([float(f) for f in focus])
        self.target = numpy.array([float(t) for t in target])
        self.field_of_view = float(field_of_view)

    def print_self(self):
        print("V_res: ", self.v_res)
        print("H_res: ", self.h_res)
        print("Distance: ", self.distance)
        print("Up: ", self.up)
        print("Focus: ", self.focus)
        print("Target: ", self.target)
        print("Field of View: ", self.field_of_view)

    def rotate(self,x = 0,y = 0 ,z = 0, point = (0,0,0)):
        self.focus = rotate_x(x, point, self.focus)
        self.focus = rotate_y(y, point, self.focus)
        self.focus = rotate_z(z, point, self.focus)
        self.target = rotate_x(x, point, self.target)
        self.target = rotate_y(y, point, self.target)
        self.target = rotate_z(z, point, self.target)



    def translation(self, vector):
        self.focus = [v1 + v2 for v1, v2 in zip(self.focus, vector)]

class Light:
    def __init__(self, position, intensity):
        self.position = numpy.array([float(p) for p in position])
        self.intensity = numpy.array([float(i) for i in intensity])/255

    def translation(self, vector):
        self.position = [v1 + v2 for v1, v2 in zip(self.position, vector)]

class AmbientLight:
    def __init__(self, intensity):
        self.intensity = numpy.array([float(i) for i in intensity])/255

