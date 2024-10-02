satır_sayısı = int(input("bir sayı giriniz: ")) # kullanıcıdan bir sayı al
for i in range(1, satır_sayısı +1): # girilen sayıyı 1 den başlayarak bir bir artırarak girilen sayıya kadar satır çizilir.
    print(" " * (satır_sayısı - i), end=" ") # önce boşukları yazdır
    print("*" * (2*i -1)) # sonra yıldızları belirle
