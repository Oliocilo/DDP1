nama = "Joonkok"
usia = 14

#grade
if(usia >= 65):
    grade = "Lanjut Usia"
elif(usia >= 25 and usia <= 65):
    grade = "Dewasa"
elif(usia >= 18 and usia <= 25):
    grade = "Pasca Remaja"
elif(usia >= 10 and usia <= 18):
    grade = "Remaja"
elif(usia >= 1 and usia <= 10):
    grade = "Anak-Anak"

#Data
#print("\nNama \t:",nama,"\nUsia \t:",usia,"\nKeterangan \t:",grade)

angka1 = float(input("90"))
angka2 = float(input("60"))

if angka1 > angka2:
    print(f"{angka1} lebih besar dari {angka2}")
elif angka2 > angka1:
    print(f"{angka2} lebih besar dari {angka1}")
else:
    print("Kedua angka sama besar")