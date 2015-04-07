list = [7, 4, 6, 8, 2]

def insertion_sort(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index - 1
	# Loop until the index goes all the way left
        while i >= 0:
            if value < list[i]:
                # Shift value all the way over and stuff
                list[i+1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break

insertion_sort(list)

print list
