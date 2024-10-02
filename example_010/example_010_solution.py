metin = input("Bir metin giriniz: ") #metin oluştur
kelime = metin.split() # metni boşlulardan bölerek kelimeler lstesini oluşturma
en_uzun_kelime = max(kelime, key=len) # en uzun kelimeyi bulma !!
print("en uzun kelime:", en_uzun_kelime) # yazdır
