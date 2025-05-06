'''
Primeiro Exercício: Soma de elementos pares
Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os
elementos pares contidos nela.
Exemplo: [2,4,10,3,9,7,15,22]
Saída: A soma dos pares é: x

'''

def somar_pares(lista_de_elementos):
    """
    Esta função recebe uma lista de números inteiros e retorna a soma de todos os elementos pares contidos nela.
    
    :param lista_de_elementos: Lista de números inteiros
    :return: Soma dos números pares
    """
    resultado = 0
    for numero in lista_de_elementos:
        if numero % 2 == 0:
            resultado += numero # resutado = resultado + numero
    return resultado

lista = [1, 4, 6, 10, 13, 8, 2, 9]

print(f'O resultado da soma dos elementos pares é: {somar_pares(lista)}')