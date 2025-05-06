'''
Sexto Exercício: Combinação de dicionários
Escreva uma função que recebe dois dicionários onde as chaves são strings e os valores são
inteiros. A função deve combinar os dicionários somando os valores das chaves que
aparecem em ambos.
Exemplo:
d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}
Saída: {"a": 3, "b": 7, "c": 5, "d": 7}

'''

def combinar_dicionarios (d1: dict, d2: dict):
    for chave in d1.keys():
        if chave in d2.keys():
            d2[chave] += d1[chave]
    return d2

d1 = {"a": 2, "b": 3, "c": 5, "d": 7}
d2 = {"a": 1, "b": 4, "d": 7, "e": 8}
print (combinar_dicionarios(d1, d2))