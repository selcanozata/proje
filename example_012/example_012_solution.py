liste = [4,8,78,41,2,13]  # önce liste oluştur
eleman= int(input("listeden çıkarmak istediğiniz elemanı giriniz: ")) #kullanıcıdan çıkarmak istediği elemanı al.
if eleman in liste: # eğer eleman listede var ise 
    liste.remove(eleman) # elemanı listeden çıkar remove çıkarma işlemini yapar
    print(f"yeni liste: {liste}") # elemanın çıkarılmış olduğu listeyi yazdır
else: # eleman listede yok ise
    print(f"{eleman} listede yok.") # listede yok yazdır.
