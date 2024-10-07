metin = input("bir metin giriniz:") # kullanıcıdan metin al
kelimeler = metin.split() # metni kelimelere ayırır
# son harfi büyük olan yeni kelimeler oluşturur
yeni_kelime_listesi =[kelime[:-1]+ kelime[-1].upper() if len(kelime) > 1 else kelime.upper() for kelime in kelimeler ]
yeni_metin = " ".join(yeni_kelime_listesi) #yeni kelimeleri birleştirip sonucu yazdır
print(yeni_metin)
