def binary_search(arr, item):
    if not arr:
        return None
    
    low = 0 
    high = len(arr)-1 # para consultar o indice válido não a quantidade de elementos.
    
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