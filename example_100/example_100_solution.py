metin = input("Bir metin girin: ") #kullanıcıdan bşr metin alınız
sesli_harfler = 'aeıioöuüAEIİOÖUÜ' #sesli harfler listesi
sesli_harf_sayisi = 0
#karakterleri kontrol etme
for harf in metin:
    if harf in sesli_harfler:
        sesli_harf_sayisi += 1
# Sonucu ekrana yazdırma
print("Sesli harf sayısı:", sesli_harf_sayisi)
