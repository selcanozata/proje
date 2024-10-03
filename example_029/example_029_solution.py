dizi=[4,2,10,9] #kullanıcıdan bir sayı al
sonuc = []      # dizideki her eleman sırayla 0 a kadar azaltılır
for sayi in dizi:
    for i in range(sayi, -1, -1):  # sayidan 0'a kadar azalt
        sonuc.append(i)
print("Sonuç: ", sonuc)
