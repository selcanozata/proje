metin = input("Bir metin giriniz: ")
kelimeler = metin.split() #metni kelimelere ayır
sıralanmıs_kelimeler = sorted(kelimeler) #metni alfabetik sıraya koy
print("Alfabetik sıraya göre:", " ".join(sıralanmıs_kelimeler)) 
