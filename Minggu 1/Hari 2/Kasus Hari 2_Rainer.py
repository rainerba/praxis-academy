#Kasus Hari 2 Minggu 1
#Rainer Beth Andrew

import modulhari2
ex = [12,35,56,22,3,17,15,8,20,32,63,64,23,63,42,16,23,46,54,32,26]
print("Data awal: " + str(ex))

#panggil module, function metode algoritma sorting, beserta nilai yang dibawa
#nama algoritma: bubble, insertion, selection, merge, dan quick
modulhari2.quick(ex)

#Modul hanya mengolah data tanpa menampilkan, sehingga print secara manual
print("Data Akhir:" + str(ex))