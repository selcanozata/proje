
metin= input("bir metin girin: ") # kullanıcıdan bir metin al
sesli_harfler ="aeıioöuüAEIİOÖUÜ" #sesli harfleri belirle büyük olanları unutma
yeni_metin= ""
for karakter in metin:
    if karakter in sesli_harfler:
        yeni_metin += karakter.upper() # sesli harfleri büyük yap
    else:
        yeni_metin += karakter # diğer karekterleri olduğu gibi ekle
print("Sesli harfleri büyük olan metin: ", yeni_metin) #yazdır
