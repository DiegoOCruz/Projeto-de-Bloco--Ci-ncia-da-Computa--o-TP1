import time
arquivo = '/home/diego/Documentos/listagem_arquivos.txt'


with open(arquivo, 'r') as arquivo:
    lista_arquivos = [linha.strip().replace('inflating: tp1/', '') for linha in arquivo]

print(f"Total de linhas lidas: {len(lista_arquivos)}")

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista


tamanho_entrada = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 10003]
resultados = []

#Cronometrar e ordenar com Bubble Sort

# for entrada in tamanho_entrada:
#    lista_tempo = []
#    for _ in range(10):
#        start_time = time.time()
#        ordenado_bubble = bubble_sort(lista_arquivos[:entrada].copy())
#        bubble_sort_time = time.time() - start_time
#        lista_tempo.append(bubble_sort_time)

#     #tempo médio para o tamanho atual de entrada
#    tempo_medio = sum(lista_tempo) / len(lista_tempo)
#    resultados.append((entrada, tempo_medio))
#    print(f"Tamanho da entrada: {entrada}, Tempo médio: {tempo_medio:.6f} segundos")


#-----------------------------------------------------------------------------------

 #Cronometrar e ordenar com Selection Sort

# for entrada in tamanho_entrada:
#      lista_tempo = []
#      for _ in range(10):
#          start_time = time.time()
#          ordenado_selection = selection_sort(lista_arquivos[:entrada].copy())
#          selection_sort_time = time.time() - start_time
#          lista_tempo.append(selection_sort_time)

#      # tempo médio para o tamanho atual de entrada
#      tempo_medio = sum(lista_tempo) / len(lista_tempo)
#      resultados.append((entrada, tempo_medio)) 
#      print(f"Tamanho da entrada: {entrada}, Tempo médio: {tempo_medio:.6f} segundos")


#-------------------------------------------------------------------------------------

# Cronometrar e ordenar com Insertion Sort
for entrada in tamanho_entrada:
    lista_tempo = []
    for _ in range(10):
        start_time = time.time()
        ordenado_insertion = insertion_sort(lista_arquivos[:entrada].copy())
        insertion_sort_time = time.time() - start_time
        lista_tempo.append(insertion_sort_time)

    # tempo médio para o tamanho atual de entrada
    tempo_medio = sum(lista_tempo) / len(lista_tempo)
    resultados.append((entrada, tempo_medio)) 
    print(f"Tamanho da entrada: {entrada}, Tempo médio: {tempo_medio:.6f} segundos")




