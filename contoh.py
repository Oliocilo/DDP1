x = 10
x = "nurul fikri"

#print(x)

bil1 = 3.14
bil2 = 10
hasil = bil1 * bil2

#print(type(bil1))
#print(type(bil2))
#print(hasil)

#deklarasi dan inisialisasi variabel
pelanggan = "joseph"
totalbelanja = 1000

#struktur kendali if
if(totalbelanja > 900):
    keterangan = "selamat kamu orang pertama belanja lebih dari 500 perak"
else:
    keterangan = "Cuma segini belanjanya? baiklah terima kasih"

#cetak data
#print("pelanggan",pelanggan,"\nTotal Belanja kamu Rp.",totalbelanja,"\n",keterangan)

#Siswa dinyatakan lulus minimal 40 nilainya
nama = "pawas"
matpel = "Pendidikan Agama"
nilai = 20.5
#ternary
keterangan  = "Lulus" if nilai >= 40 else "Tidak Lulus"

#Data
print("Nama Siswa \t:",nama,
"\nMata Pelajaran \t:",matpel,
"\nNilai \t:",nilai,
"\nKeterangan \t:",keterangan)
#batas

nama = "pawas"
matpel = "MTK"
nilai = 40
#uji grade dengan IF Multi Kondisi
if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >= 75 and nilai <= 85):
    grade = "B"
elif(nilai >= 60 and nilai <= 75):
    grade = "C"
elif(nilai >= 30 and nilai <= 60):
    grade = "D"
else:
    grade = "E"

#Data
#print("Nama \t:",nama,"\nMatpel \t:",matpel,"\nNilai \t:",nilai,"\nGrade \t:",grade)