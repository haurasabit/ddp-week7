nama = input("Nama Pelanggan : ")
hp = input("No Hp : ")
apaan = input("makanan/minuman? : ")


if apaan == "makanan" :
    order = input("Pesan Makanan : ")
elif apaan == "minuman" :
    order = input("Pesan Minuman : ")
    
jumlah = input("masukan jumlah pesanan : ")

print()
print("Halo,", nama, "nomor hp kamu", hp, "yaa..")
print("kamu pesan", order, "sebanyak", jumlah, "pcs")


if order == "nasi goreng" :
    print("total harga", int(jumlah)*15000, "rupiah ya!")
elif order == "mie goreng" :
    print("total harga =", int(jumlah)*12000, "rupiah ya!")
elif order == "ayam geprek" :
    print("total harga =", int(jumlah)*18000, "rupiah ya!")
    
elif order == "jus" :
    print("total harga", int(jumlah)*15000, "rupiah ya!")
elif order == "soft drink" :
    print("total harga =", int(jumlah)*10000, "rupiah ya!")
elif order == "sweet ice tea" :
    print("total harga =", int(jumlah)*5000, "rupiah ya!")
else :
    print("Maaf, item belum tersedia!")

print ()   
print("Terimakasih telah memesan di toko kami! Selamat menikmati")