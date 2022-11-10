print()
print("Halo selamat datang, kami melayani pengisian bensin..")
print("silahkan masukan kendaraan anda (motor/mobil)")
print("pilihan tujuan kota anda: jakarta, bekasi, depok, tanggerang, bogor")
print("kami melayani pertalite, pertamax, dan pertamax turbo")
print()

kendaraan = input("Kendaraan : ")
bensin = input("Jenis Bensin/Kota Tujuan : ")


print("Anda memakai", kendaraan, "dengan bensin dan tujuan", bensin,)

jtpertalite = 12
jtpertamax = 13
jtpturbo = 13.5

jakarta=20
bekasi=35.7
depok=5
tanggerang=99
bogor=120.6

pertalite = 10000
pertamax = 14000
pertamaxturbo = 17000

pb1 =jakarta/jtpertalite
pb2 =jakarta/jtpertamax
pb3 =jakarta/jtpturbo

pb4 =bekasi/jtpertalite
pb5 =bekasi/jtpertamax
pb6 =bekasi/jtpturbo

pb7 =depok/jtpertalite
pb8 =depok/jtpertamax
pb9 =depok/jtpturbo

pb10 =tanggerang/jtpertalite
pb11 =tanggerang/jtpertamax
pb12 =tanggerang/jtpturbo

pb13 =bogor/jtpertalite
pb14 =bogor/jtpertamax
pb15 =bogor/jtpturbo

print()

#PEMAKAIAN BENSIN
#pertalite
if bensin == "pertalite/jakarta" :
    print("maka anda akan memakai bensin sebanyak", pb1, "liter")
elif bensin == "pertalite/bekasi" :
    print("maka anda akan memakai bensin sebanyak", pb4, "liter")
elif bensin == "pertalite/depok" :
    print("maka anda akan memakai bensin sebanyak", pb7, "liter")
elif bensin == "pertalite/tanggerang" :
    print("maka anda akan memakai bensin sebanyak", pb10, "liter")
elif bensin == "pertalite/bogor" :
    print("maka anda akan memakai bensin sebanyak", pb13, "liter")
#pertamax
elif bensin == "pertamax/jakarta" :
    print("maka anda akan memakai bensin sebanyak", pb2, "liter")
elif bensin == "pertamax/bekasi" :
    print("maka anda akan memakai bensin sebanyak", pb5, "liter")
elif bensin == "pertamax/depok" :
    print("maka anda akan memakai bensin sebanyak", pb8, "liter")
elif bensin == "pertamax/tanggerang" :
    print("maka anda akan memakai bensin sebanyak", pb11, "liter")
elif bensin == "pertamax/bogor" :
    print("maka anda akan memakai bensin sebanyak", pb14, "liter")
#pertamax turbo
elif bensin == "pertamax turbo/jakarta" :
    print("maka anda akan memakai bensin sebanyak", pb3, "liter")
elif bensin == "pertamax turbo/bekasi" :
    print("maka anda akan memakai bensin sebanyak", pb6, "liter")
elif bensin == "pertamax turbo/depok" :
    print("maka anda akan memakai bensin sebanyak", pb9, "liter")
elif bensin == "pertamax turbo/tanggerang" :
    print("maka anda akan memakai bensin sebanyak", pb12, "liter")
elif bensin == "pertamax turbo/bogor" :
    print("maka anda akan memakai bensin sebanyak", pb15, "liter")
else :
    print("gagal input! mohon diulang kembali..")
    
    
#TOTAL HARGA BENSIN
if bensin == "pertalite/jakarta" :
    print("total harga", int(pb1)*int(pertalite), "rupiah")
elif bensin == "pertalite/bekasi" :
    print("total harga", int(pb4)*int(pertalite), "rupiah")
elif bensin == "pertalite/depok" :
    print("total harga", int(pb7)*int(pertalite), "rupiah")
elif bensin == "pertalite/tanggerang" :
    print(pb10*pertalite)
elif bensin == "pertalite/bogor" :
    print("total harga", int(pb13)*int(pertalite), "rupiah")
#pertamax
elif bensin == "pertamax/jakarta" :
    print("total harga", int(pb2)*int(pertamax), "rupiah")
elif bensin == "pertamax/bekasi" :
    print("total harga", int(pb5)*int(pertamax), "rupiah")
elif bensin == "pertamax/depok" :
    print("total harga", int(pb8)*int(pertamax), "rupiah")
elif bensin == "pertamax/tanggerang" :
    print("total harga", int(pb11)*int(pertamax), "rupiah")
elif bensin == "pertamax/bogor" :
    print("total harga", int(pb14)*int(pertamax), "rupiah")
#pertamax turbo
elif bensin == "pertamax turbo/jakarta" :
    print("total harga", int(pb3)*int(pertamaxturbo), "rupiah")
elif bensin == "pertamax turbo/bekasi" :
    print("total harga", int(pb6)*int(pertamaxturbo), "rupiah")
elif bensin == "pertamax turbo/depok" :
    print("total harga", int(pb9)*int(pertamaxturbo), "rupiah")
elif bensin == "pertamax turbo/tanggerang" :
    print("total harga", int(pb12)*int(pertamaxturbo), "rupiah")
elif bensin == "pertamax turbo/bogor" :
    print("total harga", int(pb15)*int(pertamaxturbo), "rupiah")
else :
    print("gagal input! mohon diulang kembali..")