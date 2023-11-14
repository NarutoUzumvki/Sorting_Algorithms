def sort(seq):
    for x in range(len(seq)):
        for j in range(x+1,len(seq)):
            if seq[x] > seq[j] :
                seq[x], seq[j] = seq[j], seq[x]
    return  seq


def merge(list1, list2):
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

    if i < len(list1):
        list3.extend(list1[i:])
    if j < len(list2):
        list3.extend(list2[j:])

    return list3


seq1 = [15,2,31,78,25]
get_sorted1 = sort(seq1)
print(get_sorted1)

seq2 = [45,7,82,69,9,2,23,7]
get_sorted2 = sort(seq2)
print(get_sorted2)


get_merged = merge(seq1, seq2)
print(get_merged)
 get_merged