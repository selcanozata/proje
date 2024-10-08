metin =input("Bir metin giriniz: ") #kullanıcıdan bir metin alınız
kelimeler = metin.split() #metni kelimelere ayırma
kelime_sayısı = {} #kelime sayımı
for kelime in kelimeler:
    if kelime in kelime_sayısı:
        kelime_sayısı[kelime] += 1
    else:
        kelime_sayısı[kelime]= 1
en_sık_kelime = max(kelime_sayısı,key=kelime_sayısı.get) #en sık geçen kelimeyi bulma
print(f"En sık geçen kelime: '{en_sık_kelime}'") #yazdır 75
