
sayı= input("Bir dizi sayı giriniz: ") # kullanıcıdan sayı dizisi al
sayı_listesi= list(map(int,sayı.split())) #girilen değerleri sayılara dönüştür
en_kucuk= min(sayı_listesi) # en küçük sayıyı bulur
index = sayı_listesi.index(en_kucuk) #indexini bulur
print(f"En küçük sayının indeksi: {index}") #yazdr  
