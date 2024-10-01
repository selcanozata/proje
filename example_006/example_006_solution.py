sayi = int(input("Bir Sayı Girin: "))
if sayi <= 1:
    print(f"{sayi} asal sayı değil.")
else:
    asal = True
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            asal = False
            break
if asal:
    print(f"{sayi} asal sayıdır.")
else:
    print(f"{sayi} asal sayı değil.")
  
