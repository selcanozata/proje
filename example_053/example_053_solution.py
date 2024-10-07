dizi= input("bir dizi sayı giriniz: ") #kullanıcıdan bir dizi sayı al
liste=list(map(int,dizi.split()))  #Girilen stringi sayılara dönüştür ve bir listeye ekle
print(f"Liste: {liste}")      
