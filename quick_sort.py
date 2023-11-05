# def quick_sort(seq):
#     length = len(seq)
#     if length <= 1 :
#         return seq
#     else:
#         pivot = seq.pop()
#     items_greater = []
#     items_lower = []

#     for item in seq :
#         if item > pivot :
#             items_greater.append(item)

#         else:
#             items_lower.append(item)

#     print(items_lower)
#     print(pivot)
#     print(items_greater)
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def quick_sort(seq):
    if len(seq) <= 1 :
        return seq
    else:
        pivot = seq.pop()

    lower = []
    greater = []
    for item in seq :
        if item > pivot :
            greater.append(item)

        else:
            lower.append(item)

    return quick_sort(lower) + [ pivot ] + quick_sort(greater)



# seq = [21,4,5,8,96,3,57,86,5]

seq = [15,2,78,5,6,98,65,4,23,5,458,4,46,47,1,7]
get_sorted = quick_sort(seq)
print(get_sorted)


