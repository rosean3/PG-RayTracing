# PG-RayTracing
A primeira entrega está na branch primeira-entrega.
<br>
## Funcionamento

O programa recebe um arquivo de entrada no formato txt
com as informações do mundo a ser renderizado e gera um arquivo de saída com a imagem renderizada.

## Objetos
cada objeto que possa ter no mundo esta em objetos.py, assim como as funções de interseção, normal, translação e rotação.

## Operações
As operações mais comuns para calcular que não tenham libs específicas estão em operações.py

## Renderização
A renderização é feita em trace_image.py, onde é feito o loop principal do programa, onde é feito o cálculo de interseção, normal, iluminação e cor do pixel.

## Arquivo de entrada
O arquivo de entrada deve ser um arquivo .txt que deve ser passado o caminho até ele na main.py.

## Rodar o programa
Para rodar o programa, basta passar o caminho até o arquivo de entrada na main.py e rodar e rodar a main.py.

## Testes prontos
Para usar nossos arquivos de teste é só rodar o arquivo testes.py (mas antes substitua as rotas dos txts com as rotas corretas no seu computador). As imagens geradas devem ser as mesmas que estão na pasta results.


