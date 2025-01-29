# time copmlexity: O(nlogn)  worts case: O(n^2)
# space complexity: O(n)

def quick_sort(lists: list)->list:
    if len(lists) <= 1:
        return lists
    pivot = lists.pop()
    list_left = []
    right_list = []
    for i in lists:
        if i <= pivot:
            list_left.append(i)
        else:
            right_list.append(i)
    return quick_sort(list_left) + [pivot] + quick_sort(right_list)

if __name__ == '__main__':  
    lists = [5, 2, 8, 3, 9, 12, 4, 1, 6]
    print(quick_sort(lists))
