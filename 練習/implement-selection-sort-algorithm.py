def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
       
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            
    return arr


if __name__ == '__main__':
    
    list1 = [33, 1, 89, 2, 67, 245]
    print(selection_sort(list1))  
    list2 = [5, 3, 4]
    result = selection_sort(list2)
    print(list2 is result)  