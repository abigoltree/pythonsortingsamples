array = [2,4,5,3,8,6,1,7]
print(array)

def quicksort(array):
    if len(array) > 2:
        pivot = len(array) - 2
        while array[pivot + 1] > array[pivot]:
            temp = array[pivot]
            #print array
	    array[pivot] = array[pivot + 1]
            array[pivot + 1] = temp
            pivot = pivot - 1

        arrayl = []
        arrayr = []
        for index in range(pivot + 1):
            arrayl[index] = array[index]

        for index in range(pivot + 1, len(array) - 1):
            arrayr[index] = array[pivot:]

        print (array)
        print (arrayl)
        print (arrayr)
        quicksort(arrayl)
        quicksort(arrayr)

quicksort(array)
print(array)
