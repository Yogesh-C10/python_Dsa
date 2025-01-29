def binary_search(arr: list, left: int, right: int, n: int) -> int:
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr: list, n: int) -> bool:
    if arr[0] == n:
        return True

    # Find range for binary search
    bound = 1
    while bound < len(arr) and arr[bound] < n:
        bound *= 2

    # Perform binary search in the identified range
    left = bound // 2
    right = min(bound, len(arr) - 1)
    return binary_search(arr, left, right, n) != -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 7

if exponential_search(arr, key):
    print("Found using Exponential Search")
else:
    print("Not found using Exponential Search")
