kalimat = input("kalimat: ")
kata = input("Kata yang dicari: ")
hitung = 0
a = kalimat.lower()
kata_yg_dicari = a.split()

for i in kata_yg_dicari:
    if i==kata:
        hitung +=1
print("Jumlah kata :",hitung)