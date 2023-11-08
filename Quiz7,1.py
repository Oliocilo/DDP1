#Quiz No.2
# Menu makanan
menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Geprek": 18000,
}

# Menu minuman
menu_minuman = {
    "Aneka Jus": 15000,
    "Soft Drink": 10000,
    "Sweet Ice Tea": 5000,
}

# Input data
nama_pembeli = input("Masukan Nama Pembeli: ")
no_hp_pembeli = input("Masukan No Hp Pembeli: ")
jenis_pesanan = input("""Pesan Menu Apa? (Makanan atau Minuman): """)

# Perhitungan
if jenis_pesanan == "makanan,Makanan,makan,Minum":
    pilihan_menu = input("Masukkan pesanan: ")
    jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
    harga_pesanan = menu_makanan[pilihan_menu] * jumlah_pesanan
elif jenis_pesanan == "minuman,Minuman,minum,Minum":
    pilihan_menu = input("Masukkan pesanan: ")
    jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
    harga_pesanan = menu_minuman[pilihan_menu] * jumlah_pesanan

# Output
print("Nama Pembeli:", nama_pembeli)
print("No Hp Pembeli:", no_hp_pembeli)
print("Menu yang di Pesan:", pilihan_menu)
print("Jumlah pesanan:", jumlah_pesanan)
print("Harga yang harus di bayarkan:", harga_pesanan)