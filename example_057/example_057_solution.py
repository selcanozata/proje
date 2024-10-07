kelime= input("Bir dizi kelime giriniz: ") #kullanıcıdan dizi şeklinde kelimeler al
kelime_listesi= kelime.split() #girilen kelimeleri bir listeye dönüştür
en_uzun_kelime= max(kelime_listesi, key=len) # en uzun kelimeyi bul
print(f"En uzun kelime: {en_uzun_kelime.strip()}") #sonucu yazdır  
