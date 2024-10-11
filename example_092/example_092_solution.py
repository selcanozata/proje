dizi = input("Bir dizi eleman giriniz : ").split() #kullanıcıdan dizi alma
dizi = [int(i) for i in dizi] #elemanları tam sayı yapar
tekrarlar = {}

for eleman in dizi: #her elemanın kaç kez geçtiğini bul
    if eleman in tekrarlar:
        tekrarlar[eleman] += 1
    else:
        tekrarlar[eleman] = 1

# Sonuçları ekrana yazdırma
for eleman, tekrar in tekrarlar.items():
    print(f"{eleman}: {tekrar}")   
