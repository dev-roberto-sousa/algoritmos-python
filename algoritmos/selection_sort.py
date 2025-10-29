def findSmallest(arr):
    if not isinstance(arr, list):
        return None 

    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    if not isinstance(arr, list):
        return None 
    
    newArr = []
    copiedArr =  list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr


unsorted_list = [23, 4, 56, 38, 55, 1]
print(selectionSort(unsorted_list))