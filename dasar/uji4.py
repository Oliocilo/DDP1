import math

def hitung_luas_persegi(sisi):
    return sisi ** 2

def hitung_luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

def hitung_luas_segitiga(alas, tinggi):
    return 1/2 * alas * tinggi

def main():
    print("Program Menghitung Luas Bangun Datar")
    print("Pilih bangun datar yang ingin dihitung luas:")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")

pilihan = input("""
        *** PILIHAN OPERASI ***
        1. HITUNG PERSEGI
        2. HITUNG LINGKARAN
        3. HITUNG SEGITIGA
       """)

match pilihan:
    case "1":
        s = int(input("masukkan sisi: "))
        persegi = s*s
        print('luas persegi', persegi)
    case "2":
        phi = 3.14
        r = int(input("masukkan jari: "))
        lingkaran = phi*r*r
        print('luas lingkaran', lingkaran)
    case "3":
        l = 1/2
        a = int(input("masukkan alas: "))
        t = int(input("masukkan tinggi: "))
        segitiga = l*a*t
        print('luas lingkaran', segitiga)
    case _:
        print("pilihan tidak tersedia")