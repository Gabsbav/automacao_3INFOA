''' 
as funções permite modularizar o codigo, dividir ele em partes menores que podem ser reaproveitadas. isso simplifica a codificação

Estrutura função em python

def nome_funcao(param1, param2, paramN):
    //algumn codig que a função faz 
    return valor_retornado
'''

#cria uma função que calcula a area do triângulo

def calTriangleArea(base, altura):
   area = (base*altura) / 2
   return area 

def calSquareArea(lado):
   area = (lado*lado) 
   return area 

'''
area1 = calTriangleArea(100, 10)
print("A area do triangulo 1 é ", area1)

base = float = (input('digite a base: '))
altura = float(input('digite a altura: '))
area1 = calTriangleArea(base, altura)
print("A area do triangulo 1 é ", area1)
'''
