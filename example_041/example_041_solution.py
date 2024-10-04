sayı_dizisi = input("Sayı dizisi giriniz: ") #kullanıcıdan sayı dizisi al
sayi_listesi =list(map(int, sayı_dizisi.split())) #sayıları ayırıp bir liste oluştur
tek_toplam= sum(sayi for sayi in sayi_listesi if sayi % 2 !=0) #tek sayıların toplamını hesaplama
print(f"Tek sayıların toplamı: {tek_toplam}") #yazdır
