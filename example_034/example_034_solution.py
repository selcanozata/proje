sayi_dizisi= input("Sıralamak istediğiniz sayıları giriniz: ") #kullanıcıdan sayı listesi al
sayi_listesi = list(map(int,sayi_dizisi.split())) # girilen sayıları listeye çevirir
siralama= sorted(sayi_listesi, reverse= True) # büyükten küçüğe sıralar
print("Sıralanan liste:" , siralama) #yazdır
