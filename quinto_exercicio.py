'''
Quinto Exercício: Tupla de médias
Dado um dicionário onde as chaves são nomes de alunos e os valores são listas com suas
notas, crie uma função que retorna uma lista de tuplas, onde cada tupla contém o nome do
aluno e sua média de notas.
Exemplo: {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
Saída: [("Ana", 8.0), ("Bruno", 5.33), ("Carlos", 9.67)]

'''

def calcular_medias (notas: dict):
    lista_medias = []
    for chave, valor in notas.items():
        media = round((valor[0] + valor[1] + valor[2]) / len(valor), 2) 
        lista_medias.append( (chave, media) )
    return lista_medias

notas = {'Samuel': [10,9,10], 'Karynne': [10,10,10], 'Carol': [5,4,7]}
print (calcular_medias(notas))