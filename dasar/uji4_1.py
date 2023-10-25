# Membuat list dengan nilai awal
minuman = ['Ale-ale' , '190ml' , 'anggur']

# Menambahkan nilai [harga kendaraan, tipe kendaraan] di belakang list
minuman += ['Rp 1.000', 'minumanmanis']

# Menyisipkan [merkkendaraan] setelah 'JenisKendaraan'
indeks = minuman.index('minumanmanis')
minuman.insert(indeks + 1, 'Ale-ale')

# Menampilkan isi list kendaraan
print(minuman)