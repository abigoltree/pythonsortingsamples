#merge sort algorithm

a = [2,4,6,1,3,8,7,5]
print (a)

def merge(a, lefth, righth):
        i = 0
        j = 0
        k = 0
        while i < len(lefth) and j < len(righth):
            if lefth[i] < righth[j]:
                a[k] = lefth[i]
                i = i + 1
            else:
                a[k] = righth[j]
                j = j + 1
            k = k + 1

        while i < len(lefth):
                a[k] = lefth[i]
                i = i + 1
                k = k + 1
       
        while j < len(righth):
                a[k] = righth[j]
                j = j + 1
                k = k + 1

def merge_sort(a):
    if len(a) > 1:
        mid = len(a)//2
        lefth = a[:mid]
        righth = a[mid:]
        
        merge_sort(lefth)
        print(lefth)
        print(righth)
        merge_sort(righth)
        merge(a, lefth, righth)

#    len(a)
#    if len(a) < 2:
#        return a
#    midL = midpoint(a)
#    for index in range(0,midL):
#        aL[index = a[index]
#    midR = len(a) - midpoint(a)
merge_sort(a)      
print (a)
