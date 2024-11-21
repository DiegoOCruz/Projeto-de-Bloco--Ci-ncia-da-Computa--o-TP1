import time
from collections import deque
from memory_profiler import memory_usage

def medir_desempenho(func):
    def wrapper(*args, **kwargs):
        tempo = []
        memoria = []
        for i in range(10):
            start_time = time.time()
            mem_inicial = memory_usage()[0]
            resultado = func(*args, **kwargs)
            final_time = time.time() - start_time
            mem_final = memory_usage()[0]
            tempo.append(final_time)
            memoria.append(mem_final - mem_inicial)
        print(f"Tempo médio de execução: {(int(sum(tempo))/(len(tempo))):.6f} segundos")
        print(f"Uso de médio de memória: {(int(sum(memoria))/(len(memoria))):.2f} MiB")
        return resultado
    return wrapper

arquivo = '/home/diego/Documentos/listagem_arquivos.txt'
arquivo_posicao_insercao = '/home/diego/Documentos/posicao_insercao.txt'

with open(arquivo, 'r') as arquivo:
    lista_arquivos = [linha.strip().replace('inflating: tp1/', '') for linha in arquivo]

print(f"Total de linhas lidas: {len(lista_arquivos)}")

with open(arquivo_posicao_insercao, 'r') as arquivo:
    lista_arquivos_posicao_insercao = [linha.strip().replace('inflating: tp1/', '') for linha in arquivo]

print(f"Total de linhas lidas: {len(lista_arquivos_posicao_insercao)}")


def hashtable(lista):
    hashtable = {}
    for i, item in enumerate(lista, 1):
        if i not in hashtable:
            hashtable[i] = []
        hashtable[i].append({"item": item})
    return hashtable


def pilha(lista):
    pilha = []
    for item in lista:
        pilha.append(item)
    return pilha


class Fila:
    def __init__(self):
        self.itens = []

    def add(self, item):
        self.itens.append(item)

    def remove(self):
        if not self.is_empty():
            return self.itens.pop(0)
        return "Fila vazia"

    def is_empty(self):
        return len(self.itens) == 0

    def size(self):
        return len(self.itens)

    def acessar_item(self, posicao):
        if posicao < 0 or posicao >= len(self.itens):
            return "Posição fora dos limites da fila."

        temp = []  # Fila auxiliar para armazenar os itens removidos
        item_desejado = None

        # Remove os itens até chegar à posição desejada
        for i in range(len(self.itens)):
            item = self.remove()
            if i == posicao:
                item_desejado = item
            temp.append(item)

        for item in temp:
            self.add(item)

        return item_desejado

@medir_desempenho
def tarefa_1():
    armazenamento_hastable = hashtable(lista_arquivos)
    print("-="*30)
    print("Recuperacao hashtable:")
    print(f'posicao 1: {armazenamento_hastable[1]}')
    print(f'posicao 100: {armazenamento_hastable[100]}')
    print(f'posicao 1000: {armazenamento_hastable[1000]}')
    print(f'posicao 5000: {armazenamento_hastable[5000]}')  
    print("-="*30)

@medir_desempenho
def tarefa_2():
    armazenamento_pilha = pilha(lista_arquivos)
    print("-="*30)
    print("Recuperacao pilha:")
    print(f'posicao 1: {armazenamento_pilha[0]}')
    print(f'posicao 100: {armazenamento_pilha[99]}')
    print(f'posicao 1000: {armazenamento_pilha[999]}')
    print(f'posicao 5000: {armazenamento_pilha[4999]}')

    print("-="*30)

@medir_desempenho
def tarefa_3():
    fila = Fila()
    for i in lista_arquivos:
        fila.add(i)
    print("-="*30)
    print("Recuperacao fila:")
    print(f'posicao 1: {fila.acessar_item(0)}')
    print(f'posicao 100: {fila.acessar_item(99)}')
    print(f'posicao 1000: {fila.acessar_item(999)}')
    print(f'posicao 5000: {fila.acessar_item(4999)}')
    print("-="*30)

#tarefa_1()
#tarefa_2()
tarefa_3()


