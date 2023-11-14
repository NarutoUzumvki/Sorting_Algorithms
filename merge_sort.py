# def merge(list1,list2):
#     i = 0
#     j = 0
#     list3 = []
#     while i < len(list1) and j < len(list2) :
#         if list2[j] < list1[i] :
#             list3.append(list2[j])
#             j += 1

#         else :
#             list3.append(list1[i])
#             i += 1

#     if i < len(list1) :
#         list3.extend(list1[i:])
#     if j < len(list2) :
#         list3.extend(list2[j:])

#     return list3


# def divide(seq):
#     if len(seq) == 1 :
#         return seq
#     mid = len(seq) // 2
#     l = divide(seq[:mid])
#     r = divide(seq[mid:])

#     return merge(l,r)


# def divide(seq):
#     if len(seq) == 1 :
#         return seq
#     mid = len(seq) // 2
#     l = divide(seq[:mid])
#     r = divide(seq[mid:])
#     return merge(l,r)



def merge(seq1,seq2):
    i = 0
    j = 0
    seq3 = []
    while i < len(seq1) and j < len(seq2):
        if seq1[i] < seq2[j] :
            seq3.append(seq1[i])
            i+=1

        else:
            seq3.append(seq2[j])
            j+=1

    if  i < len(seq1) :
        seq3.extend(seq1[i:])

    if j < len(seq2) :
        seq3.extend(seq2[j:])

    return seq3


def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2
    l = merge_sort(seq[:mid])
    r = merge_sort(seq[mid:])

    return merge (l,r)


# list1 = [21,5,19,8,37,72,3,5]
list1 = [12,57,6,8,9,2,33,1,3422,68,12,228,7,47,5,2,4,7,89,6,21,5]
get_merged = merge_sort(list1)
# get_merged = divide(list1)
print(get_merged)