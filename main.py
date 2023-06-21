import random
import math

def calcular_distancia(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia


def calcular_custo(percurso, grafo):
    custo_total = 0
    for i in range(len(percurso) - 1):
        cidade_atual = percurso[i]
        proxima_cidade = percurso[i + 1]
        custo_total += grafo[(cidade_atual, proxima_cidade)]
    return custo_total
def gerar_vizinhos(solucao_atual):
    vizinhos = []
    n = len(solucao_atual)

    for i in range(n):
        for j in range(i + 1, n):
            vizinho = solucao_atual[:]
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            vizinhos.append(vizinho)

    return vizinhos


def hill_climbing_iterativo(vertices, grafo):
    solucao_atual = list(vertices.keys())  # Converter as chaves do dicionário em uma lista

    while True:
        melhor_vizinho = None
        melhor_custo = float('inf')

        # Gerar todos os vizinhos da solução atual
        for vizinho in gerar_vizinhos(solucao_atual):
            custo_vizinho = calcular_custo(vizinho, grafo)
            if custo_vizinho < melhor_custo:
                melhor_vizinho = vizinho
                melhor_custo = custo_vizinho

        # Verificar se a melhor solução encontrada é melhor que a atual
        if melhor_custo < calcular_custo(solucao_atual, grafo):
            solucao_atual = melhor_vizinho
        else:
            break

    return solucao_atual




def simulated_annealing(vertices, grafo, temperatura_inicial, taxa_resfriamento):
    solucao_atual = list(vertices.keys())  # Converter as chaves do dicionário em uma lista
    melhor_solucao = solucao_atual.copy()
    melhor_custo = calcular_custo(solucao_atual, grafo)

    temperatura = temperatura_inicial

    while temperatura > 0.01:
        cidade1, cidade2 = random.sample(solucao_atual, 2)
        vizinho = solucao_atual.copy()
        vizinho[vizinho.index(cidade1)], vizinho[vizinho.index(cidade2)] = cidade2, cidade1

        custo_vizinho = calcular_custo(vizinho, grafo)
        custo_atual = calcular_custo(solucao_atual, grafo)

        if custo_vizinho < custo_atual:
            solucao_atual = vizinho.copy()
            if custo_vizinho < melhor_custo:
                melhor_solucao = solucao_atual.copy()
                melhor_custo = custo_vizinho
        else:
            probabilidade = math.exp((custo_atual - custo_vizinho) / temperatura)
            if random.random() < probabilidade:
                solucao_atual = vizinho.copy()

        temperatura *= taxa_resfriamento

    return melhor_solucao


# Leitura do arquivo de entrada
def ler_arquivo(nome_arquivo):
    vertices = {}
    grafo = {}

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            if linha.strip().isdigit():
                break

            valores = linha.strip().split()
            if len(valores) != 3:
                continue

            id, x, y = valores
            x = float(x)
            y = float(y)

            vertices[int(id)] = (x, y)

        for i, cidade_atual in enumerate(vertices.keys()):
            for j, proxima_cidade in enumerate(vertices.keys()):
                if j <= i:
                    continue

                distancia = calcular_distancia(vertices[cidade_atual], vertices[proxima_cidade])
                grafo[(cidade_atual, proxima_cidade)] = distancia
                grafo[(proxima_cidade, cidade_atual)] = distancia

    return vertices, grafo





import glob

if __name__ == '__main__':
    nomes_arquivos = glob.glob('*.txt')  # Lista todos os arquivos .txt no diretório atual

    temperatura_inicial = 100.0  # Defina a temperatura inicial correta
    taxa_resfriamento = 0.99  # Defina a taxa de resfriamento correta

    for nome_arquivo in nomes_arquivos:
        print("Arquivo:", nome_arquivo)

        # Leitura do arquivo de entrada
        vertices, grafo = ler_arquivo(nome_arquivo)

        # Execução do Hill Climbing Iterativo
        melhor_percurso_hc = hill_climbing_iterativo(vertices, grafo)

        # Execução do Simulated Annealing
        melhor_percurso_sa = simulated_annealing(vertices, grafo, temperatura_inicial, taxa_resfriamento)

        print("Melhor percurso (Hill Climbing Iterativo):", melhor_percurso_hc)
        print("Melhor percurso (Simulated Annealing):", melhor_percurso_sa)
        print()




