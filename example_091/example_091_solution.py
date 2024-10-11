import random

kullanici_metin = input("Bir metin girin: ") #kullanıcıdan bir metin alınız
harfler = list(kullanici_metin) #metni harflere ayırır
random.shuffle(harfler) #harfleri karıştırır
karisik_metin = ''.join(harfler) #karışmış harfleri birleştirir
print("Karışık metin:", karisik_metin) # yeni metni yazdırır  
