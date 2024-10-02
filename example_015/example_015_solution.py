liste = [4,4,8,7,6,5,5] # listeyi oluştur
tekil_elemanlar= [x for x in liste if liste.count(x)==1]  # liste.count(x) fonksiyonu ile tekil elemanlar bulunur.
print(tekil_elemanlar) # yazdır
