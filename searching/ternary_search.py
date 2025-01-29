def ternary_search(arr: list, n: int) -> bool:
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Divide the range into three parts
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Check if the element is at one of the mid-points
        if arr[mid1] == n or arr[mid2] == n:
            return True
        
        # Narrow the search space
        if n < arr[mid1]:
            right = mid1 - 1  # Search in the left part
        elif n > arr[mid2]:
            left = mid2 + 1  # Search in the right part
        else:
            left = mid1 + 1
            right = mid2 - 1  # Search in the middle part

    return False

# Example usage
arr = [1, 2, 3, 4, 5]
key = 2

if ternary_search(arr, key):
    print("Found using Ternary Search")
else:
    print("Not found using Ternary Search")
