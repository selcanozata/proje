metin = input("bir metin giriniz: ") #kullanıcıdan metin al
kelimeler= metin.split()  #metini boşluklara ayırıyoruz
kelime_sayısı = len(kelimeler) # kelime sayısını bul
print(f"Kelime sayısı: {kelime_sayısı}") # sonucu ekrana yazdır 
