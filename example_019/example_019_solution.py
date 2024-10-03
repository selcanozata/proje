liste = [1,8,7,9,45,78,90] # listeyi oluşturun
liste.sort()               # listeyi sıralama
n = len(liste)             # listenin uzunluğunu hesaplama
if n % 2 == 1:             # ortanca sayıyı bulma
    ortanca = liste[n // 2] # tek sayıda ise
else:
    ortanca = (liste[n// 2-1] + liste[n//2]) / 2  # çift sayıda ise
print("ortanca sayı: ", ortanca) # yazdırma
