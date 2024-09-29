def binary_search(to_search, target):  
    low = 0  
    high = len(to_search) - 1  
    mid = 0  

    while low <= high:  
        mid = (high + low) // 2  

        if to_search[mid] < target:  
            low = mid + 1  
        elif to_search[mid] > target:  
            high = mid - 1
            
        else:
            return True  

    return False
