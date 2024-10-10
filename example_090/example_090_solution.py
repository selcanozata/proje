sayi = int(input("Bir sayı girin: "))
faktoriyel = 1  #faktöriyel hesaplama
for i in range(1, sayi + 1):
    faktoriyel *= i

print(f"{sayi}! = {faktoriyel}")
