sayi_dizisi = input("Sayı dizisi oluşturun: ") #kullanıcıdan sayıları al
sayi_listesi = list(map(int, sayi_dizisi.split())) #sayıları listeye çevir
toplam = sum(sayi_listesi) #sayıların toplamı
uzunluk = len(sayi_listesi) #kaç sayı girildiği
ortalama = toplam / uzunluk # ortalama hesaplama
print(f"Ortalama: {ortalama}") #yazdır
