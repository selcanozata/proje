metin = input("Bir metin girin: ") # kullanıcıdan metin al
kelimeler = metin.split() #metni kelimelere ayır 
kelime_uzunlukları= [len(kelime) for kelime in kelimeler] #her kelimenin uzunluğunu bul ve liste oluştur
print("," .join(map(str, kelime_uzunlukları))) # yazdır   
