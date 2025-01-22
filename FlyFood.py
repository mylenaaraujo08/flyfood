from math import factorial
import time

import os
import itertools

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Função para ler o mapa e processar as coordenadas
def ler_mapa(arquivo):
    with open(arquivo, "r") as file:
        linhas, colunas = map(int, file.readline().split())
        linhas = file.read().splitlines()
        coordenadas = {}
        origem = None
        for i, linha in enumerate(linhas):
            for j, valor in enumerate(linha.split()):
                if valor == "R":
                    origem = (i, j)
                elif valor != "0":
                    coordenadas[valor] = (i, j)

        pontos = [coordenadas[chave] for chave in coordenadas]
    return pontos, coordenadas, origem

# chama a função que constrói as permutações
def gerar_permutacao(pontos):
    trajetos = [None] * factorial(len(pontos))
    indice = [0]
    permutacao([], pontos, trajetos, indice)
    return trajetos

# constrói as permutações e retorna uma lista com todos os caminhos
def permutacao(permutacao_atual, pontos_restantes, trajetos, indice):
    if not pontos_restantes:
        trajetos[indice[0]] = permutacao_atual
        indice[0] += 1
    else:
        for i in range(len(pontos_restantes)):
            nova_permutacao = permutacao_atual + [pontos_restantes[i]]

            restante = [None] * (len(pontos_restantes)-1)
            c = 0
            for j in range(len(pontos_restantes)):
                if j != i:
                    restante[c] = (pontos_restantes[j])
                    c += 1
            permutacao(nova_permutacao, restante, trajetos, indice)
    return trajetos


# calcula a distância de todos os caminhos construídos e retorna o menor entre eles
def manhattan(lista_trajetos, origem):
    menor_distancia = 100
    menor_caminho = None

    for trajeto in lista_trajetos:
        ultimo = len(trajeto)-1
        distancia_total = abs(origem[0] - trajeto[0][0]) + abs(origem[1] - trajeto[0][1])

        for indice in range(len(trajeto) - 1):
            p1 = trajeto[indice]
            p2 = trajeto[indice + 1]
            distancia_total += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        distancia_total += abs(trajeto[ultimo][0] - origem[0]) + abs(trajeto[ultimo][1] - origem[1])

        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            menor_caminho = trajeto
    return menor_caminho, menor_distancia


inicio = time.time()
arquivo_mapa = 'Trajeto.txt'
p, c, origem = ler_mapa(arquivo_mapa)
trajetos_totais = gerar_permutacao(p)
otimo, dronometro = manhattan(trajetos_totais, origem)

# Substitui a chamada da função `converter`
print(dronometro)
caminho_otimo = ' '.join(
    chave for coordenada in otimo for chave, valor in c.items() if valor == coordenada
)

print(caminho_otimo)
final = time.time()
print(f'Tempo necessário: {final - inicio}')
