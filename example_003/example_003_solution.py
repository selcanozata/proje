metin = input("Bir Metin Girin: ")
sesli_harfler = "aeuoi"
sayac = 0
for harf in metin:
    if harf in sesli_harfler:
        sayac += 1
print("Sesli Harflerin Sayısı: ", sayac)
