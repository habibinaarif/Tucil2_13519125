import os

# fungsi untuk menghitung derajat setiap simpul
def derajat(arr):
    return [len(arr[i])-1 for i in range(len(arr))]

# prosedur menghapus elemen dalam array
def hapus(el, arr):
    # menghapus simpul
    for i in range(len(arr)):
        if arr[i][0] == el:
            arr.pop(i)
            break

    # menghapus busur simpul
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == el:
                arr[i].pop(j)
                break

# menerima input dari folder test
cur_dir = os.path.dirname(os.path.realpath(__file__))
new_dir = cur_dir[:len(cur_dir)-3]+'test\\'
namafile = input("Masukkan nama file: ")
f = open(new_dir+namafile)

data = f.read()
baris = data.split('\n')

kode = []
for row in baris:
    kode.append(row[:-1].split(', '))

# Mengurutkan kode mata kuliah
order = []
while len(kode) > 0:

    # menghitung derajat simpul
    degree = derajat(kode)

    # Mengambil yang derajatnya 0 dan tambahkan ke order
    ambil = []
    for k in range(len(degree)):
        if degree[k] == 0:
            ambil.append(kode[k][0])
    order.append(ambil)

    # Menghapus kode mata kuliah yang diambil
    for a in ambil:
        hapus(a,kode)
  
# Menuliskan keluaran program           
for i in range(len(order)):
    print("Semester "+str(i+1)+":", end =' ')
    for j in range(len(order[i])-1):
        print(order[i][j], end = ', ')
    print(order[i][len(order[i])-1])

# menerima sembarang input agar dapat menampilkan output pada file .exe
dummy = input() 