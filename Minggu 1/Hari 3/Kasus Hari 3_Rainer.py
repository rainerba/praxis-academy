#Kasus Hari 1 Minggu 1
#Rainer Beth Andrew

#Contoh data yang akan diurutkan:
ex = [12,35,56,22,3,17,15,8,20,32,63,64,23,63,42,16,23,46,54,32,26]
print("Data awal: " + str(ex))

class sorting:
    def __init__(self, data):
        self.data = data

    def bubble(self):
        n = len(self.data)
        for i in range(n-1):
            for j in range(n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

    def insertion(self):
        n = len(self.data)
        for i in range(1, n):
            temp = self.data[i]
            j = i-1
            while j>=0 and temp < self.data[j]:
                self.data[j+1] = self.data [j]
                j-=1
            self.data[j+1] = temp

    def selection(self):
        for i in range(len(self.data)):
            temp = self.data[i]
            pointer = i
            for j in range(i, len(self.data)):
                if self.data[j]<temp:
                    temp = self.data[j]
                    pointer = j
            tukar = self.data[i]
            self.data[i] = temp
            self.data[pointer] = tukar

    def merge(self):
        if len(self.data) > 1:
            mid = len(self.data) // 2
            L = self.data[:mid]
            kiri = sorting(L)
            R = self.data[mid:]
            kanan = sorting(R)
            kiri.merge()
            kanan.merge()
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    self.data[k] = L[i]
                    i += 1
                else:
                    self.data[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                self.data[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                self.data[k] = R[j]
                j += 1
                k += 1

    def quick(self):
        if len(self.data) > 1:
            pointer = 0
            pivot = self.data[-1]
            for i in range(len(self.data)-2):
                if self.data[i] > pivot:
                #detect nilai > pivot
                    for j in range(i, len(self.data)-1):
                        if self.data[j] < pivot:
                        #detect nilai yang akan ditukar
                            temp = self.data[j]
                            self.data[j] = self.data[i]
                            self.data[i] = temp
                            pointer = i
            self.data[-1] = self.data[pointer+1]
            self.data[pointer+1] = pivot
            L = self.data[:pointer+1]
            kiri = sorting(L)
            R = self.data[pointer+1:]
            kanan = sorting(R)
            kiri.quick()
            kanan.quick()
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    self.data[k] = L[i]
                    i += 1
                else:
                    self.data[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                self.data[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                self.data[k] = R[j]
                j += 1
                k += 1

#pilih algoritma sorting dengan mengubah quick dengan function yang diinginkan
sorting(ex).quick()

print("Data Akhir:" + str(ex))