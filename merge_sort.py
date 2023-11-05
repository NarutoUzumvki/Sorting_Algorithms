def merge(list1,list2):
    i = 0
    j = 0
    list3 = []
    while i < len(list1) and j < len(list2) :
        if list2[j] < list1[i] :
            list3.append(list2[j])
            j += 1

        else :
            list3.append(list1[i])
            i += 1

    if i < len(list1) :
        list3.extend(list1[i:])
    if j < len(list2) :
        list3.extend(list2[j:])

    return list3


# def divide(seq):
#     if len(seq) == 1 :
#         return seq
#     mid = len(seq) // 2
#     l = divide(seq[:mid])
#     r = divide(seq[mid:])

#     return merge(l,r)


def divide(seq):
    if len(seq) == 1 :
        return seq
    mid = len(seq) // 2
    l = divide(seq[:mid])
    r = divide(seq[mid:])
    return merge(l,r)

list1 = [21,5,19,8,37,72,3,5]
get_merged = divide(list1)
print(get_merged)
