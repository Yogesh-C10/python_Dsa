def merge_sort(lists:list)->list:
    if len(lists) <= 1:
        return lists
    mid = len(lists) // 2
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result       

if __name__ == '__main__':  
    lists = [5, 2, 8, 3, 9, 12, 4, 1, 6]
    print(merge_sort(lists))