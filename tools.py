from objetos import *

def getInput(file_location):
    f = open(file_location, 'r')
    linha = 0

    objects = {}
    scene = {}

    while (1):
        line = f.readline().replace('\n', '').split()
        linha +=1

        if not line:
            return objects, scene

        #pega os dados da esfera
        if line[0] == 's':
            if 'sphere' not in objects:
                objects['sphere'] = []

            if len(line) != 14:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros da esfera esta correto na linha ", linha)
                return
            else:
                center = numpy.array([float(x) for x in line[1:4]])
                radius = float(line[4])
                objects['sphere'].append(
                    Sphere(center, radius, line[5:8], line[8], line[9], line[10], line[11], line[12], line[13]))

        #pega os dados do plano
        elif line[0] == 'p':
            if 'plane' not in objects:
                objects['plane'] = []

            if len(line) != 16:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros do plano esta correto na linha ", linha)
                return
            else:
                point = numpy.array([int(x) for x in line[1:4]])
                normal = numpy.array([int(x) for x in line[4:7]])
                objects['plane'].append(
                    Plane(point, normal, line[7:10], line[10], line[11], line[12], line[13], line[14], line[15]))

        #pega os dados da camera
        elif line[0] == 'c':
            if len(line) != 13:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros da camera esta correto na linha ", linha)
                return
            else:
                h_res = int(line[1])
                v_res = int(line[2])
                d = float(line[3])
                up = numpy.array([float(x) for x in line[4:7]])
                focus = numpy.array([float(x) for x in line[7:10]])
                target = numpy.array([float(x) for x in line[10:13]])
                scene['camera'] = Camera(h_res, v_res, d, up, focus, target)

        #pega os dados da luz
        elif line[0] == 'l':
            if 'light' not in scene:
                scene['light'] = []

            if len(line) != 7:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros da luz esta correto na linha ", linha)
                return

            else:
                position = numpy.array([float(x) for x in line[1:4]])
                scene['light'].append(Light(position, line[4:7]))

        #pega os dados do triangulo
        elif line[0] == 't':
            if 'triangle_mesh' not in objects:
                objects['all_triangles'] = []


            n_faces, n_vertices = line[1:3]
            vertices, faces = [], []
            for i in range(int(n_vertices)):
                line = f.readline().replace('\n', '').split()
                linha += 1
                if len(line) != 3:
                    print("Erro na leitura do arquivo\nVerifique se o numero de vertices esta correto na linha ", linha)
                    return
                else:
                    vertices.append(line)

            for i in range(int(n_faces)):
                line = f.readline().replace('\n', '').split()
                linha += 1
                if len(line) != 3:
                    print("Erro na leitura do arquivo\nVerifique se o numero de faces esta correto na linha ", linha)
                    return
                else:
                    faces.append(line)

            line = f.readline().replace('\n', '').split()
            linha += 1

            if len(line) != 9:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros do triangulo esta correto na linha ", linha)
                return

            else:
                auxMesh = TriangleMesh(faces, vertices, line[0:3], line[3], line[4], line[5], line[6], line[7],line[8])
                objects['all_triangles'] = numpy.append(objects['all_triangles'], auxMesh.generate_triangles())

        #pega os dados da luz ambiente
        elif line[0] == 'a':
            if len(line) != 4:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros da luz ambiente esta correto na linha ", linha)
                return
            else:
                ambient_intensity = numpy.array([int(x) for x in line[1:4]])
                scene['ambient'] = AmbientLight(ambient_intensity)