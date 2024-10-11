sayi = int(input("Bir sayı girin: ")) #kulanıcıdan sayı alma
if sayi % 5 == 0:  # 5 ile bölünüp bölümdeğinin kontrol edilmesi
    print(f"{sayi}, 5 ile tam bölünüyor.")
else:
    print(f"{sayi}, 5 ile tam bölünmüyor.")  
