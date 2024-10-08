dizi = [3,4,5]  #dizi oluştur
#yeni dizi oluştur toplam için gerekli
yeni_dizi = []
toplam = 0
#dizideki her elemanı topla yeni diziye ekleme
for sayi in dizi:
    toplam += sayi
    yeni_dizi.append(toplam)
#yazdır
print(f"Kümülatif toplam listesi: {yeni_dizi}") 
