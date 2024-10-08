import random 
metin = input("Bir metin giriniz: ") #bir metin alın 
harfler = list(metin) #harfleri listeye çeviriyoruz
random.shuffle(harfler) #harfleri karıştırma
karışık_metin = "".join(harfler) #karıştırılmış harfleri birleştirme
print(f"Karışık metin: {karışık_metin}") 
