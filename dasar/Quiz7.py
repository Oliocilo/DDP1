#Quiz no.1
harga = 17000

#uji grade dengan IF Multi Kondisi
if(harga >= 17000 and harga <= 17000):
    grade = "Pertamax Turbo/Liter"
    grade1 = "13.5 KM"
elif(harga >= 14000 and harga <= 17000):
    grade = "Pertamax/Liter"
    grade1 = "13 KM"
elif(harga >= 10000 and harga <= 14000):
    grade = "Pertalite/Liter"
    grade1 = "12 KM"
else:
    grade = "Belum masukkan harga"

#Data
#print("\nHarga \t:",harga,"\nJenis Bensin \t:",grade,"\nDengan jarak tempuh \t:",grade1)

# Jenis bensin
hargabensin = {
    "Pertalite": 10000,
    "Pertamax": 14000,
    "Pertamax Turbo": 17000,
}

# Jarak tempuh per liter
jaraktempuh = {
    "Pertalite": 12,
    "Pertamax": 13,
    "Pertamax Turbo": 13.5,
}

# Jarak kota
jarakkota = {
    "Jakarta": 20,
    "Bekasi": 35.7,
    "Depok": 5,
    "Tangerang": 99,
    "Bogor": 120.6,
}

# Input data
nama_kendaraan = input("Tipe kendaraan: ")
jenis_bensin = input("Jenis bensin: ")
kota_tujuan = input("Kota tujuan: ")

# Perhitungan
konsumsi_bensin = jarakkota[kota_tujuan] / jaraktempuh[jenis_bensin]
biaya_bensin = konsumsi_bensin * hargabensin[jenis_bensin]

# Output
print("Tipe kendaraan:", nama_kendaraan)
print("Jenis bensin:", jenis_bensin)
print("Kota tujuan:", kota_tujuan)
print("Konsumsi bensin:", int(konsumsi_bensin), "liter")
print("Biaya bensin:", int(biaya_bensin), "rupiah")