n = int (input("bir sayı giriniz: ")) # bir sayı al kullanıcıdan
a,b = 0,1  #ilk iki fibonacci sayısı
if n == 1:
    print(f"{n}. fibonacci sayısı: {a}")
elif n== 2:    # sayı 1 ve 2 ise direkt sonucu yazdır
    print(f"{n}. fionacci sayısı: {b}")
else:
    for i in range(2,n):  #  asıl yer burası girilen değer hesaplanır.
        a,b = b, a+b
    print(f"{n}. fibonacci sayısı: {b}")
  
