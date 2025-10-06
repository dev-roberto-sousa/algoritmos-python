""" 
# Busca Binária: Encontrando um Número em uma Lista Ordenada
A busca binária é um método eficiente para encontrar a posição
de um número específico em uma lista ordenada. Imagine que você
tem uma lista de números organizados do menor para o maior.

**Como funciona:**

Você começa examinando o elemento do meio da lista.
Se esse elemento for exatamente o número que você está procurando, a busca termina.
Se o número procurado for menor que o elemento do meio, você descarta a metade superior
da lista e repete o processo apenas na metade inferior.
Se for maior, você descarta a metade inferior e continua apenas com a metade superior.
A cada passo, você reduz o problema pela metade. Em uma lista com 1.000 elementos, 
esse método encontra qualquer elemento em no máximo 10 verificações, pois 2 elevado a 10 é 1.024.
"""


def binary_search(arr, item):
    if not arr:
        return None
    
    low = 0 
    high = len(arr)-1 # para consultar o indice válido, não a quantidade de elementos.
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = list(range(1000))

print(binary_search(my_list, 300)) # 300
print(binary_search(my_list, -1)) # None
print(binary_search(my_list, 1001)) # None