metin = input("Bir metin girin: ") #kullanıcıdan bir metn al
kelimeler = metin.split() #kelimelere ayırır
tekrarlar = {} #boş bir sözlük oluşturur

# Her kelimenin kaç kez geçtiğini bul
for kelime in kelimeler:
    if kelime in tekrarlar:
        tekrarlar[kelime] += 1
    else:
        tekrarlar[kelime] = 1


en_sik_kelimeler = max(tekrarlar, key=tekrarlar.get) #en çok tekrarlanan kelimeyi bulur
print(f"En sık geçen kelime: '{en_sik_kelimeler}'") 
