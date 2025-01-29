pos = -1  

def lin_search(arr: list, key: int) -> int:
    global pos 
    pos = 0 
    
    for i in arr:
        if i == key:
            return True
        pos += 1  # Increment position for each element

    return -1  # Return -1 if the key is not found

arr = [1,2,3,4,5]
key =2

if lin_search(arr,key):
    print(pos+1)