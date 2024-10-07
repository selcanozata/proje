metin = input("Bir metin girin: ") #kullanıcıdan bir metin al
ters_kelime= [kelime[::-1] for kelime in metin.split()] #metni kelimelere ayır sonra her kelimeyi ters çevir
ters_metin= " ".join(ters_kelime) #yazdır
print(ters_metin)   
