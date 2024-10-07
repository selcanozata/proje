sayilar = list(map(int,input("Bir dizi sayı girin: ").split())) #kullanıcıdan sayıları al ve listeye çevir
iki_katı= [sayi*2 for sayi in sayilar] #her sayının 2 katını alır yeni bir liste oluşturur
print(iki_katı) #yeni listeyi yazdırır
