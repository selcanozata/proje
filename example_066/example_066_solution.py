metin = input("Bir metin girin: ") #kullanıcıdan metin al
kelimeler = metin.split()  # Boşluklara göre ayırma
kelimeler.sort()  # Alfabetik sıraya koyma
print("Alfabetik sıraya göre: " + ' '.join(kelimeler))    
