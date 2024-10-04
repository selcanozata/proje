sayi_dizisi = input("Sayı dizisi oluşturun: ") #kullanıcıdan sayıları al
sayi_listesi =  sayi_dizisi.split() #sayıları listeye çevir
tekrar_sayilari= {} #elemanların tekrar sayısını tutmak için ir sözlük oluştur
for sayi in sayi_listesi:
    if sayi in tekrar_sayilari:
        tekrar_sayilari[sayi] += 1 #sayı varsa bir artır
    else:
        tekrar_sayilari[sayi] = 1 #sayı yoksa 1 olarak başlat

for sayi, tekrar in tekrar_sayilari.items():
    print(f"{sayi}: {tekrar}") 
