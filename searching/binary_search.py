def bi_search(arr: list,n: int)-> int:
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) //2
        if arr[mid] == n:
            return True
        elif arr[mid] < n:
            left = mid +1
        else:
            right = mid-1
    return False
arr = [1,2,3,4,5]
key =2

if bi_search(arr,key):
    print("hi")
else:
    print("not found")