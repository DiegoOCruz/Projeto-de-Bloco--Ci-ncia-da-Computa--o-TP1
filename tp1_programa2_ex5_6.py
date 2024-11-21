import time
from collections import deque
from memory_profiler import memory_usage
import random

def medir_desempenho(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_inicial = memory_usage()[0]
        resultado = func(*args, **kwargs)
        final_time = time.time() - start_time
        mem_final = memory_usage()[0]
        print(f"Tempo de execução: {final_time:.6f} segundos")
        print(f"Uso de memória: {mem_final - mem_inicial:.2f} MiB")
        return resultado
    return wrapper

def substitui_repetidos(lista):
    valores_unicos = set()

    for i in range(len(lista)):
        while lista[i] in valores_unicos:
            lista[i] = random.randint(1, 10000)

        valores_unicos.add(lista[i])


    if len(valores_unicos) < len(lista):
        return substitui_repetidos(lista)
    for i in lista:
        if i == '':
            lista.remove(i)

    return lista

arquivo = '/home/diego/Documentos/listagem_arquivos.txt'
arquivo_posicao_insercao = '/home/diego/Documentos/posicao_insercao.txt'
arquivo_texto_insercao = '/home/diego/Documentos/nome_insercao.txt'
arquivo_posicao_remocao = '/home/diego/Documentos/posicao_remocao.txt'

with open(arquivo, 'r') as arquivo:
    lista_arquivos = [linha.strip().replace('inflating: tp1/', '') for linha in arquivo]

#print(f"Total de linhas lidas: {len(lista_arquivos)}")
#------------------------------------------------------------------------------------------------------------

with open(arquivo_posicao_insercao, 'r') as arquivo:
    lista_arquivos_posicao_insercao = substitui_repetidos([linha.strip() for linha in arquivo])

#print(f"Total de linhas lidas: {len(lista_arquivos_posicao_insercao)}")

#------------------------------------------------------------------------------------------------------------

with open(arquivo_texto_insercao, 'r') as arquivo:
    lista_arquivos_texto_insercao = [linha.strip() for linha in arquivo]

#print(f"Total de linhas lidas: {len(lista_arquivos_texto_insercao)}")

#------------------------------------------------------------------------------------------------------------

with open(arquivo_posicao_remocao, 'r') as arquivo:
    lista_arquivos_posicao_remocao = substitui_repetidos([linha.strip() for linha in arquivo])

#print(f"Total de linhas lidas: {len(lista_arquivos_posicao_remocao)}")

#------------------------------------------------------------------------------------------------------------


def hashtable(lista):
    hashtable = {}
    for i, item in enumerate(lista, 1):
        if i not in hashtable:
            hashtable[i] = []
        hashtable[i].append({item})
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
        # Adiciona um item no final da fila
        self.itens.append(item)

    def remove(self):
        # Remove e retorna o item do início da fila
        if not self.is_empty():
            return self.itens.pop(0)
        return "Fila vazia"

    def is_empty(self):
        # Retorna True se a fila estiver vazia
        return len(self.itens) == 0

    def size(self):
        # Retorna o tamanho da fila
        return len(self.itens)

    def localizar_e_alterar(self, posicao, novo_valor):
        # Verifica se a posição é válida
        if posicao < 0 or posicao >= len(self.itens):
            return "Posição fora dos limites da fila."

        temp = []  # Fila temporária para armazenar os itens removidos
        item_alterado = None

        # Remove itens até encontrar a posição desejada
        for i in range(posicao):
            temp.append(self.remove())  # Remove os itens até a posição desejada

        # Altera o item na posição desejada
        item_alterado = self.remove()  # Este é o item a ser alterado
        self.add(novo_valor)  # Enfileira o novo valor no lugar do antigo

        # Reenfileira os itens removidos
        for item in temp:
            self.add(item)

        #return f"Item '{item_alterado}' na posição {posicao} foi alterado para '{novo_valor}'."

    def remover_item(self, posicao):
        # Verifica se a posição é válida
        if posicao < 0 or posicao >= len(self.itens):
            return "Posição fora dos limites da fila."

        temp = []  # Fila auxiliar para armazenar os itens removidos
        item_removido = None

        # Remove os itens até chegar à posição desejada
        for i in range(len(self.itens)):
            item = self.remove()
            if i == posicao:
                item_removido = item  # Guarda o item a ser removido
            else:
                temp.append(item)  # Armazena o item na fila temporária

        # Reinsere os itens de volta na fila original, exceto o removido
        for item in temp:
            self.add(item)

        return f"Item '{item_removido}' na posição {posicao} foi removido."



tamanho_entrada = [2,4,6,8,16,32,64,128,256,400]
resultados = []

#----------------------------------------
#HashTable - adição de valores na lista
lista_hash_table = hashtable(lista_arquivos)

@medir_desempenho
def insercao_hashTable():
    for entrada in tamanho_entrada:
        lista_tempo = []
        for _ in range(10):
            start_time = time.time()
            for posicao, texto in zip(lista_arquivos_posicao_insercao[:entrada], lista_arquivos_texto_insercao[:entrada]):
                posicao = int(posicao)
                if posicao in lista_hash_table:
                    lista_hash_table[posicao] = [texto]
            insercao_hashTable_time = time.time() - start_time
            lista_tempo.append(insercao_hashTable_time)

        tempo_medio = sum(lista_tempo) / len(lista_tempo)
        resultados.append((entrada, tempo_medio))
        print(f'Tamanho entrada: {entrada} - tempo médio: {tempo_medio:.6f} segundos')

#insercao_hashTable()

@medir_desempenho
def remocao_hashTable():
 for entrada in tamanho_entrada:
        lista_tempo = []
        for _ in range(10): 
            start_time = time.time()
            posicoes_remocao = [int(posicao) for posicao in lista_arquivos_posicao_remocao[:entrada]]
            for posicao in posicoes_remocao:
                if posicao in lista_hash_table:  
                    lista_hash_table[posicao] = []  
                else: print(f'{posicao} nao existe')
                    
            remocao_hashTable_time = time.time() - start_time
            lista_tempo.append(remocao_hashTable_time)

        tempo_medio = sum(lista_tempo) / len(lista_tempo)
        print(f'Tamanho entrada: {entrada} - tempo médio de remoção de conteúdo: {tempo_medio:.6f} segundos')
        

#remocao_hashTable()
#-----------------------------------------------------------------------------------------------------------------------

#Pilha - adição de valores na lista
lista_pilha = pilha(lista_arquivos)
@medir_desempenho
def insercao_pilha():
    for entrada in tamanho_entrada:
        lista_tempo = []
        for _ in range(10):
            start_time = time.time()
            for posicao, texto in zip(lista_arquivos_posicao_insercao[:entrada], lista_arquivos_texto_insercao[:entrada]):
                posicao = int(posicao)
                if 0 <= posicao < len(lista_pilha):
                    lista_pilha[posicao] = texto
            lista_pilha_time = time.time() - start_time
            lista_tempo.append(lista_pilha_time)

        tempo_medio = sum(lista_tempo) / len(lista_tempo)
        resultados.append((entrada, tempo_medio))
        print(f'Tamanho entrada: {entrada} - tempo médio: {tempo_medio:.6f} segundos')
    return lista_pilha

#insercao_pilha()

#Pilha - remoção de valores na lista
@medir_desempenho
def remocao_pilha():
    for entrada in tamanho_entrada:
        lista_tempo = []
        for _ in range(10):
            start_time = time.time()
            posicoes_remocao = [int(posicao) for posicao in lista_arquivos_posicao_remocao[:entrada]]
            for posicao in posicoes_remocao:
                lista_pilha[posicao] = []  
            remocao_pilha_time = time.time() - start_time
            lista_tempo.append(remocao_pilha_time)

        tempo_medio = sum(lista_tempo) / len(lista_tempo)
        print(f'Tamanho entrada: {entrada} - tempo médio de remoção de conteúdo: {tempo_medio:.6f} segundos')

#remocao_pilha()
#-----------------------------------------------------------------------------------------------------------------------

#Fila - adição de valores na lista
fila = Fila()
for item in lista_arquivos:
    fila.add(item)
#print(f"Total de itens na fila: {fila.size()}")
@medir_desempenho
def insercao_fila():
    for entrada in tamanho_entrada:
        lista_tempo = []
        for _ in range(10):
            start_time = time.time()
            for posicao, texto in zip(lista_arquivos_posicao_insercao[:entrada], lista_arquivos_texto_insercao[:entrada]):
                posicao = int(posicao)
                fila.localizar_e_alterar(posicao, texto)
                lista_fila_time = time.time() - start_time
            lista_tempo.append(lista_fila_time)

        tempo_medio = sum(lista_tempo) / len(lista_tempo)
        resultados.append((entrada, tempo_medio))
        print(f'Tamanho entrada: {entrada} - tempo médio: {tempo_medio:.6f} segundos')

#insercao_fila()

@medir_desempenho
def remocao_fila():
    for entrada in tamanho_entrada:
        lista_tempo = []
        for _ in range(10):
            start_time = time.time()
            for posicao in lista_arquivos_posicao_remocao[:entrada]:
                posicao = int(posicao)
                fila.remover_item(posicao)
                lista_fila_time = time.time() - start_time
            lista_tempo.append(lista_fila_time)

        tempo_medio = sum(lista_tempo) / len(lista_tempo)
        resultados.append((entrada, tempo_medio))
        print(f'Tamanho entrada: {entrada} - tempo médio de remoção: {tempo_medio:.6f} segundos')

remocao_fila()


