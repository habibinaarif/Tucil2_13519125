import os

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

    degree = [len(kode[i])-1 for i in range(len(kode))] # Menghitung derajat setiap matkul

    # Mengambil yang derajatnya 0 dan tambahkan ke order
    ambil = []
    for k in range(len(degree)):
        if degree[k] == 0:
            ambil.append(kode[k][0])
    order.append(ambil)

    # Menghapus kode mata kuliah yang diambil
    for a in ambil:
        for i in range(len(kode)):
            for j in range(1,len(kode[i])):
                if kode[i][j] == a:
                    kode[i].pop(j)
                    break
        for i in range(len(kode)):
            if kode[i][0] == a:
                kode.pop(i)
                break
  
# Menuliskan keluaran program           
for i in range(len(order)):
    print("Semester "+str(i+1)+":", end =' ')
    for j in range(len(order[i])-1):
        print(order[i][j], end = ', ')
    print(order[i][len(order[i])-1])