def activity_selection(lists):
    lists =sorted(lists, key = lambda lists:lists[1])
    selected = [lists[0]]
    for st, end in lists[1:]:
        if st >= selected[-1][1]:
            selected.append([st,end])
    return selected

lists = [[1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [5, 9]]
print(activity_selection(lists))