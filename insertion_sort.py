# def insertion_sort(seq):
#     for i in range(1,len(seq)):
#         j = i
#         while seq[j-1] > seq[j] and j > 0 :
#             # print(seq[j-1])
#             # print(seq[j])
#             # print("****")
#             seq[j-1], seq[j] = seq[j], seq[j-1]
#             # print(seq[j-1])
#             # print(seq[j])
#             # print("****")
#             j -= 1
#     return seq



# def insertion_sort(seq):
#     for i in range(1, len(seq)):
#         j = i-1
#         while seq[j] > seq[j+1] and j >= 0 :
#             seq[j+1], seq[j] = seq[j], seq[j+1]
#             j -= 1

#     return seq


def insertion_sort(seq):
    for i in range(1,len(seq)):
        j = i
        while seq[j-1] > seq[j] and j > 0:
            seq[j-1] , seq[j] = seq[j] , seq[j-1]
            j -= 1

    return seq

seq = [12,1,59,8,3,45,7,6,7]
get_sorted = insertion_sort(seq)
print(get_sorted)



# def insertion(seq):
#     for i in range(1,len(seq)) :
#         j = i
#         while seq[j-1] > seq[j] and j > 0:
#             seq[j-1],seq[j] = seq[j] ,seq[j-1]
#             j-=1

#     return seq

# seq = [12,1,59,18,30,45,7,16,7]
# print(insertion(seq))