from objetos import *


f = open('teste.txt', 'r')
linha = 0

if __name__ == "__main__":
    objetos = {}

    while (1):
        line = f.readline().replace('\n', '').split()
        linha +=1

        if not line:
            break

        #pega os dados da esfera
        if line[0] == 's':
            if 'sphere' not in objetos:
                objetos['sphere'] = []

            if len(line) != 14:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros da esfera esta correto na linha ", linha)
                break
            else:
                objetos['sphere'].append(
                    Sphere(line[1:4], line[4], line[5:8], line[8], line[9], line[10], line[11], line[12], line[13]))

        #pega os dados do plano
        elif line[0] == 'p':
            if 'plane' not in objetos:
                objetos['plane'] = []

            if len(line) != 16:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros do plano esta correto na linha ", linha)
                break
            else:
                objetos['plane'].append(
                    Plane(line[1:4], line[4:7], line[7:10], line[10], line[11], line[12], line[13], line[14], line[15]))

        #pega os dados da camera
        elif line[0] == 'c':
            if len(line) != 13:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros da camera esta correto na linha ", linha)
                break
            else:
                objetos['camera'] = Camera(line[1], line[2], line[3], line[4:7], line[7:10], line[10:13])

        #pega os dados da luz
        elif line[0] == 'l':
            if 'light' not in objetos:
                objetos['light'] = []

            if len(line) != 7:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros da luz esta correto na linha ", linha)
                break

            else:
                objetos['light'].append(Light(line[1:4], line[4:7]))

        #pega os dados do triangulo
        elif line[0] == 't':
            if 'triangle' not in objetos:
                objetos['triangle'] = []


            n_faces, n_vertices = line[1:3]
            vertices, faces = [], []
            for i in range(int(n_vertices)):
                line = f.readline().replace('\n', '').split()
                linha += 1
                if len(line) != 3:
                    print("Erro na leitura do arquivo\nVerifique se o numero de vertices esta correto na linha ", linha)
                    break
                else:
                    vertices.append(line)

            for i in range(int(n_faces)):
                line = f.readline().replace('\n', '').split()
                linha += 1
                if len(line) != 3:
                    print("Erro na leitura do arquivo\nVerifique se o numero de faces esta correto na linha ", linha)
                    break
                else:
                    faces.append(line)

            line = f.readline().replace('\n', '').split()
            linha += 1

            if len(line) != 9:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros do triangulo esta correto na linha ", linha)
                break

            else:
                objetos['triangle'].append(TriangleMesh(faces, vertices, line[0:3], line[3], line[4], line[5], line[6], line[7],line[8]))

        #pega os dados da luz ambiente
        elif line[0] == 'a':
            if len(line) != 4:
                print("Erro na leitura do arquivo\nVerifique se o numero de parametros da luz ambiente esta correto na linha ", linha)
                break
            else:
                objetos['ambient'] = AmbientLight(line[1:4])

    print(objetos)




