sesli_harfler = "aeıioöuüAEIİOÖUÜ"  # Türkçe sesli harfler 
sayac = 0
girdi = input("Bir metin girin: ") #kullanıcıdan bir metin alma
for harf in girdi: #her harfi kontrol et
    if harf in sesli_harfler:
        sayac += 1

print(f"Metindeki sesli harf sayısı: {sayac}") 
