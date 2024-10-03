sayi= int(input("bir sayı giriniz: ")) # kullanıcıdan sayı al

if sayi > 0 and (sayi & (sayi -1)) == 0: # 2'nin kuvveti mi ?
    print("bu sayı 2'nin kuvvetidir.")
else:
    print("bu sayı 2'nin kuvveti değildir.")
