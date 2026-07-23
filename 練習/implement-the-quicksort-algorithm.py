def quick_sort(arr):
    if len(arr) <= 1:
        return list(arr)
    
    pivot = arr[0]
    
  
    less = [x for x in arr if x < pivot]     
    equal = [x for x in arr if x == pivot]    
    greater = [x for x in arr if x > pivot]   

    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == '__main__':
    print(quick_sort([]))  # -> []
    
    original = [20, 3, 14, 1, 5]
    sorted_res = quick_sort(original)
    print(f"元のリスト: {original}")  
    print(f"ソート後  : {sorted_res}")  
    
    print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))  