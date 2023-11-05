# def selection_sort(seq):
#     for i in range(len(seq)):
#         min_index = i
#         for j in range(i+1,len(seq)):
#             if seq[j] < seq[min_index] :
#                 min_index = j
#         if min_index != i :
#             seq[i], seq[min_index] = seq[min_index], seq[i]

#     return seq


def selection_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[min_index] :
                min_index = j

        if min_index != i :
            seq[i],seq[min_index] = seq[min_index],seq[i]

    return seq

# seq = [9,23,4,52,16,98,4,53]
seq = [14,5,8,67,2,48,3,59,6,4,7,52]
get_sorted = selection_sort(seq)
print(get_sorted)
