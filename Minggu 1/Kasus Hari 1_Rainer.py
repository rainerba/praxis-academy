#Kasus Hari 1 Minggu 1
#Rainer Beth Andrew

ex = [12,35,56,22,3,17,15,8,20,32,63,64,23,63,42,16,23,46,54,32,26]
print("Data awal: " + str(ex))
print("Jumlah data: " + str(len(ex)))

def bubble(sort):
    n = len(sort)
    for i in range(n-1):
        for j in range(n-i-1):
            if sort[j] > sort[j+1]:
                sort[j], sort[j+1] = sort[j+1], sort[j]
    print(sort)

def insertion(sort):
    n = len(sort)
    for i in range(1, n):
        temp = sort[i]
        j = i-1
        while j>=0 and temp < sort[j]:
            sort[j+1] = sort [j]
            j-=1
        sort[j+1] = temp
    print(sort)

def selection(sort):
    for i in range(len(sort)):
        temp = sort[i]
        pointer = i
        for j in range(i, len(sort)):
            if sort[j]<temp:
                temp = sort[j]
                pointer = j
        tukar = sort[i]
        sort[i] = temp
        sort[pointer] = tukar
    print(sort)

def mergesort(sort):
    if len(sort) > 1:
        mid = len(sort) // 2
        L = sort[:mid]
        R = sort[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sort[k] = L[i]
                i += 1
            else:
                sort[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            sort[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            sort[k] = R[j]
            j += 1
            k += 1
    print('Proses:')
    print(sort)

def quicksort(sort):
    if len(sort) > 1:
        pointer = 0
        pivot = sort[-1]
        for i in range(len(sort)-2):
            if sort[i] > pivot:
            #detect nilai > pivot
                for j in range(i, len(sort)-1):
                    if sort[j] < pivot:
                    #detect nilai yang akan ditukar
                        temp = sort[j]
                        sort[j] = sort[i]
                        sort[i] = temp
                        pointer = i
        sort[-1] = sort[pointer+1]
        sort[pointer+1] = pivot
        L = sort[:pointer+1]
        R = sort[pointer+1:]
        quicksort(L)
        quicksort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sort[k] = L[i]
                i += 1
            else:
                sort[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            sort[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            sort[k] = R[j]
            j += 1
            k += 1

#pilih algoritma sorting
quicksort(ex)

print("Data Akhir:" + str(ex))