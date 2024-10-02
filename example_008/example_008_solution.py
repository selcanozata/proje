sayi = int(input("bir sayı giriniz: ")) # ilk önce sayı girişi oluştur
faktoriyel = 1 # bir olarak belirle sayıya doğru artarak gidecek
if sayi < 0: # negatifte çalışmaz uyarısı
    print("negatif sayıların faktöriyeli hesaplanmaz.")
elif sayi == 0: # 0 ise sayımız 
    print("0! = 1")
else:
    for i in range(1, sayi + 1): # sayımız pozitif bir sayı ise 1 den 1 er artarak girilen sayıya kadar çrparak git 
        faktoriyel *= i
    print(f"{sayi}! = {faktoriyel}") 
