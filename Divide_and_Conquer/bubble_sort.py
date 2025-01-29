def bubble_sort(lists):
    for i in range(len(lists) - 1):
        for j in range(len(lists) - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists

if __name__ == '__main__':  
    lists = [5, 2, 8, 3, 9, 12, 4, 1, 6]
    print(bubble_sort(lists))