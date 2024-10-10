dizi = [2, 5, 9]  #önceden tanımlı dizi
yeni_liste = [] #yeni liste
toplam = 0 #geçici toplamı başlat
for eleman in dizi: # dizideki her elemanı topla ve yeni listeye ekle
    toplam += eleman
    yeni_liste.append(toplam)
print(yeni_liste) #yazdır   
