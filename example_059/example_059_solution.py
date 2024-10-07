metin= input("Bir metin giriniz: ") #kullanıcıdan bir metin alınız
kelimeler = metin.split() #metni kelimelere ayır
toplam = 0 #toplamı başlat
for kelime in kelimeler:
    if kelime.isdigit(): # eğer kelime bir sayıysa toplama ekle
        toplam += int(kelime)
print(f"Toplam: {toplam}") #sonucu yazdır 
