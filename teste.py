from objetos import *

f = open('teste.txt')
line = f.readline()
if line[0] == 't':
    line = line.replace('\n', '').split()
    n_faces = int(line[1])
    n_vertices = int(line[2])

vertices = [f.readline().replace('\n', '').split() for vertice in range(n_vertices)]
faces = [f.readline().replace('\n', '').split() for face in range(n_faces)]

t1 = TriangleMesh(faces, vertices, (255,255,255), 0.1, 0.2, 0.3, 0.4, 0.5, 0.6)

print(t1.printTriangles())