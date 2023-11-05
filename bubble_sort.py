def bubble_sort(num_list):
    for i in range(len(num_list)-1,0,-1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp

    return num_list


# def bubble_sort(arr):
# 	n = len(arr)
# 	k = n
# 	for i in range(n):
# 		for j in range(1, k):
# 			if arr[j] < arr[j-1]:
# 				arr[j], arr[j-1] = arr[j-1], arr[j]
# 		k -= 1
#         # print(k)

# if __name__ == '__main__':
# 	arr = [1, 9, 5, 4, 11, 19, 3, 15]
# 	print(arr)
# 	bubble_sort(arr)
# 	print(arr)


def search(num_list,value):
	# value_idx = 0
	for x in range(len(num_list)) :
		# print(x)
		# if value in num_list:
		# 	# print(x)
		# 	value_idx = num_list[x]
		# 	print(value_idx)
		# 	return True

		if value in num_list :
			print(num_list[x])
			return True
			
		else:
			return False


num_list = [17, 5, 12, 4, 95, 32, 7, 1]
get_sorted = bubble_sort(num_list)
print(f"The Sorted list for the list is : {get_sorted} ")

search_list = search(num_list,5)
print(search_list)