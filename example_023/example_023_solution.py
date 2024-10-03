from datetime import datetime

#kullanıcıdan iki tarih alınız
tarih1 = input("İlk tarihi girin (YYYY-AA-GG): ")  
tarih2 = input("İkinci tarihi girin (YYYY-AA-GG): ")

#girilen tarihleri datetime nesnesine çeviriyoruz
tarih1_date= datetime.strptime(tarih1, "%Y-%m-%d")
tarih2_date= datetime.strptime(tarih2, "%Y-%m-%d")

# hesaplama ve yazdırma 
gun_sayisi = (tarih2_date - tarih1_date).days
print("Gün sayısı farkı:", gun_sayisi)
