sayi= int(input("Bir sayı giriniz: ")) # kullanıcıdan sayı alma
faktöriyel = 1 #faktöriyel hesaplama
for i in range (1, sayi + 1): # 1'den sayıya kadar olan sayıları çarpma
    faktöriyel *= i
print(f"{sayi}! = {faktöriyel}") 
