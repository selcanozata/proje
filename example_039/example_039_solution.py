metin= input("Bir metin giriniz: ") #kullanıcıdan metin alınız
sesli_harfler = "aeiouAEIOU" #sesli harfler listei
bulunan_sesli_harfler=[] #sesli harfleri tutmak için bir liste oluştur
# her karekteri kontrol et
for karakter in metin:
    if karakter in sesli_harfler:
        bulunan_sesli_harfler.append(karakter) #sesli harfleri listeye ekle

if bulunan_sesli_harfler: #yazdır
    print("Sesli harfler:", ',' .join(bulunan_sesli_harfler))
else:
    print("Sesli harf bulunamadı.")
