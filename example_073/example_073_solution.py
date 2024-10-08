girdi = input("Bir dizi giriniz: ") # kullanıcıdan dizi al
dizi= [int(x) for x in girdi.split()] #aldığın diziyi listeye dönüştürme
sayım={} #sayım burda başlıyor
for eleman in dizi:
    if eleman in sayım:
        sayım[eleman] += 1
    else:
        sayım[eleman]= 1
for eleman, sayi in sayım.items(): #sonuçları yazdırma
    print(f"{eleman}: {sayi}")  
