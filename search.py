def sort(seq):
    for x in range(len(seq)):
        for y in range(x+1,len(seq)):
            if seq[y] < seq[x] :
                seq[y] , seq[x] = seq[x] , seq[y]

    return seq

def linear_search(seq, value) :
    for x in range(len(seq)):
        if seq[x] == value :
            index = x 
            print(f"The index of the Value {value} is {index} .")
            return True

    return False

seq = [14,5,6,89,2,76,3,7]
get_sorted = sort(seq)
print(get_sorted)

search = linear_search(seq,5)
print(search)