sayilar = list(map(int,input("Bir dizi sayı girin: ").split())) #kullanıcıdan sayıları al ve listeye çevir
en_buyuk_sayi= sayilar.index(max(sayilar)) #en buyuk sayıyı bul ve indexini al 
print(en_buyuk_sayi) #index değerini yazdır 
