def linear_search(arr, target):
    for i in range(len(arr)):      # n iterações
        if arr[i] == target:         # O(1) por iteração
            return i
    return -1

arr = [12,3,4,6]
print(linear_search(arr, 4))