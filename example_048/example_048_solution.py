metin= input("Bir metin giriniz: ")
buyuk_harf= sum(1 for harf in metin if harf.isupper()) # BÜYÜK HARFLERİ SAYAR 
print("Büyük harf sayısı: ", buyuk_harf)   
