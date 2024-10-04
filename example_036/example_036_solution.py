sayi_dizisi= input("Sayı dizisini giriniz: ") # kullanıcıdan sayı dizisi al
sayi_listesi = list(map(int,sayi_dizisi.split())) # girilen sayıları listeye çevir
en_küçük=min(sayi_listesi) #en küçük ve en büyük sayıyı bul
en_büyük=max(sayi_listesi)
print(f"En küçük sayı: {en_küçük}") #yazdır
print(f"En büyük sayı. {en_büyük}")
