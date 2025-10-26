def pr(l, m, i, e):
    return (l - m) + (i - e)

def rata(pr, lw):
    return pr / lw

def status(rata):
    if rata >= 100:
        return "Penduuk Sehat"
    else:
        return "Kekurangan Penduduk"


l = int(input("Masukkan Angka Lahir: "))
m = int(input("Masukan Angka Kematian: "))
i = int(input("Masukkan Angka Imigrasi: "))
e = int(input("Masukkan Angka Emegrasi: "))
lw = int(input("Masukkan Luas wilayah (Dalam satuan Km persegi): "))

total = pr(l, m, i, e)
rata_final = rata(total , lw)
hasil = status(rata_final)

print("Total penduduk:", total)
print("Rata-Rata Penduduk:", rata_final)
print("Status Penduduk:", hasil)