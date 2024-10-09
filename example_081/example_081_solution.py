metin = input("bir metin giriniz: ") #kullanıcıdan bir metin alın
sesli_harfler = "aeıioöuüAEIİOÖUÜ" #sesli harfleri tanımla
sesli_harf_sayısı = 0 #sesli harf sayacını başlat
for harf in metin: #metindeki harfleri kontrol et
    if harf in sesli_harfler:
        sesli_harf_sayısı+= 1
print("Metindeki sesli harf sayısı: ", sesli_harf_sayısı) #sonucu ekrana yazdır
