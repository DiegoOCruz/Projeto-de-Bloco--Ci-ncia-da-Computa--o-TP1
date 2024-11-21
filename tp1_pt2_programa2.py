import time
from collections import deque

arquivo = '/home/diego/Documentos/listagem_arquivos.txt'

with open(arquivo, 'r') as arquivo:
    lista_arquivos = [linha.strip().replace('inflating: tp1/', '') for linha in arquivo]

print(f"Total de linhas lidas: {len(lista_arquivos)}")

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

def fila(lista):
    fila = deque()
    for item in lista:
        fila.append(item)
    return fila


def tarefas():
    try:
        armazenamento_hastable = hashtable(lista_arquivos)
        armazenamento_pilha = pilha(lista_arquivos)
        armazenamento_fila = fila(lista_arquivos)
        print("Tarefas concluídas com sucesso!")  
    except Exception as e:
        print(f"Erro ao executar as tarefas: {e}")
    return tarefa_ex3(armazenamento_hastable, armazenamento_pilha, armazenamento_fila)

def tarefa_ex3(hashtable, pilha, fila):
    print("-="*30)
    print("Recuperacao hashtable:")
    start_time = time.time()
    print(f'posicao 1: {hashtable[1]}')
    print(f'posicao 100: {hashtable[100]}')
    print(f'posicao 1000: {hashtable[1000]}')
    print(f'posicao 5000: {hashtable[5000]}')
    final_time = time.time() - start_time
    print(f"Tempo de execução: {final_time:.6f} segundos\n")
    print("-="*30)
    print("")
    print("-="*30)
    print("Recuperacao pilha:")
    start_time = time.time()
    print(f'posicao 1: {pilha[0]}')
    print(f'posicao 100: {pilha[99]}')
    print(f'posicao 1000: {pilha[999]}')
    print(f'posicao 5000: {pilha[4999]}')
    final_time = time.time() - start_time
    print(f"Tempo de execução: {final_time:.6f} segundos\n")
    print("-="*30)
    print("")
    print("-="*30)
    print("Recuperacao fila:")
    start_time = time.time()
    print(f'posicao 1: {fila[0]}')
    print(f'posicao 100: {fila[99]}')
    print(f'posicao 1000: {fila[999]}')
    print(f'posicao 5000: {fila[4999]}')
    final_time = time.time() - start_time
    print(f"Tempo de execução: {final_time:.6f} segundos\n")
    print("-="*30)
    print("")


tarefas()




