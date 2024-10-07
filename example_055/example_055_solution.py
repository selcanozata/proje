from collections import Counter

# Kullanıcıdan metin al
metin = input("Bir metin girin: ")

# Harflerin sıklığını say
harf_sayilari = Counter(metin)

# En sık geçen harfi bul
en_sik_harf = harf_sayilari.most_common(1)[0][0]

# Sonucu yazdır
print(f"En sık geçen harf: {en_sik_harf}")      
