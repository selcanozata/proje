import os

# Problemler listesini tanımla (örnek olarak)
problems = [
    "1- Kullanıcıdan bir sayı alıp, bu sayının karesini hesaplayan bir Python programı yazın. Örneğin, kullanıcı 4 girerse, program 16 yazmalı.",
    "2- Kullanıcıdan iki sayı alıp, bu sayıların toplamını bulan bir Python programı yazın. Kullanıcı 3 ve 5 girerse, program 8 yazmalı.",
    "3- Kullanıcıdan bir metin alıp, metindeki sesli harflerin sayısını bulan bir Python programı yazın. Örneğin, 'Python' için program 1 yazmalı.",
    "4- Kullanıcıdan bir kelime alıp, bu kelimenin tersini yazdıran bir Python programı yazın. Örneğin, kullanıcı 'yazılım' girerse, program 'mılızay' yazmalı.",
    "5- Bir dizideki elemanları toplayan bir Python programı yazın. Örneğin, dizi [1, 2, 3, 4] ise, program 10 yazmalı.",
    "6- Kullanıcıdan bir sayı alıp, bu sayının asal olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 7 asal bir sayıdır.",
    "7- Kullanıcıdan bir metin alıp, bu metindeki boşlukları kaldıran bir Python programı yazın. Örneğin, 'Python programı' için program 'Pythonprogramı' yazmalı.",
    "8- Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir Python programı yazın. Örneğin, 5! = 120 olmalıdır.",
    "9- Bir listede yer alan çift sayıları bulan bir Python programı yazın. Örneğin, liste [1, 2, 3, 4] ise, program [2, 4] yazmalı.",
    "10- Kullanıcıdan bir metin alıp, bu metindeki en uzun kelimeyi bulan bir Python programı yazın. Örneğin, 'Ben Python programlıyorum' için program 'programlıyorum' yazmalı.",
    "11- Kullanıcıdan bir sayı alıp, o sayının Fibonacci dizisindeki karşılığını bulan bir Python programı yazın. Örneğin, 6. Fibonacci sayısı 8'dir.",
    "12- Bir listeden belirli bir elemanı çıkaran bir Python programı yazın. Örneğin, [1, 2, 3] listesinden 2'yi çıkardığınızda [1, 3] elde edilmelidir.",
    "13- Kullanıcıdan bir metin alıp, bu metni küçük harflere dönüştüren bir Python programı yazın. Örneğin, 'PYTHON' için 'python' yazmalı.",
    "14- Kullanıcıdan bir sayı alıp, bu sayının pozitif veya negatif olduğunu kontrol eden bir Python programı yazın. Örneğin, -5 için 'negatif' yazmalı.",
    "15- Bir listede yer alan tekil elemanları (bir kez geçen elemanlar) bulan bir Python programı yazın. Örneğin, [1, 2, 2, 3] için program [1, 3] yazmalı.",
    "16- Bir dizide en sık görülen elemanı bulan bir Python programı yazın. Örneğin, [1, 1, 2, 3] için program 1 yazmalı.",
    "17- Kullanıcıdan bir sayı alıp, o sayıya göre yıldızlardan bir üçgen çizen bir Python programı yazın. Örneğin, kullanıcı 4 girerse, program 4 satırlık bir üçgen çizmelidir.",
    "18- Kullanıcıdan bir sayı alıp, bu sayının pozitif, negatif veya sıfır olduğunu kontrol eden bir Python programı yazın. Örneğin, 0 için 'sıfır' yazmalı.",
    "19- Bir listede ortanca sayıyı bulan bir Python programı yazın. Örneğin, [1, 3, 5] için program 3 yazmalı.",
    "20- Kullanıcıdan bir metin alıp, bu metindeki her kelimenin ilk harfini büyüten bir Python programı yazın. Örneğin, 'ben python öğreniyorum' için 'Ben Python Öğreniyorum' yazmalı.",
    "21- Bir listede yer alan sayıların toplamını ve ortalamasını bulan bir Python programı yazın. Örneğin, [1, 2, 3] için toplam 6, ortalama 2 yazmalıdır.",
    "22- Kullanıcıdan bir metin alıp, bu metindeki kelime sayısını bulan bir Python programı yazın. Örneğin, 'Ben program yazmayı seviyorum' için 5 yazmalıdır.",
    "23- Kullanıcıdan iki tarih alıp, bu tarihler arasındaki gün sayısını hesaplayan bir Python programı yazın. Örneğin, 2024-01-01 ile 2024-01-10 arasında 9 gün vardır.",
    "24- Bir dizideki tüm sayıları bir artan sırada sıralayan bir Python programı yazın. Örneğin, [4, 2, 3, 1] için [1, 2, 3, 4] yazmalıdır.",
    "25- Bir dizideki en küçük ve en büyük sayıyı bulan bir Python programı yazın. Örneğin, [4, 2, 3, 1] için 1 ve 4 yazmalıdır.",
    "26- Kullanıcıdan bir sayı alıp, bu sayının 2'nin kuvveti olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 8 için 'evet' yazmalı.",
    "27- Bir dizideki tüm elemanların toplamını ve ortalamasını bulan bir Python programı yazın. Örneğin, [1, 2, 3, 4] için toplam 10 ve ortalama 2.5 yazmalıdır.",
    "28- Kullanıcıdan bir kelime alıp, bu kelimenin içinde 'a' harfi olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 'ev' için 'yok' yazmalı.",
    "29- Bir dizideki sayıları sıfıra kadar azaltan bir Python programı yazın. Örneğin, [3, 2, 1] için [3, 2, 1, 0] yazmalıdır.",
    "30- Kullanıcıdan bir metin alıp, bu metnin tersini yazdıran bir Python programı yazın. Örneğin, 'Merhaba' için 'abahreM' yazmalıdır.",
    "31- Bir dizideki çift sayıların toplamını bulan bir Python programı yazın. Örneğin, [1, 2, 3, 4] için 6 yazmalıdır.",
    "32- Kullanıcıdan bir metin alıp, bu metindeki tüm sesli harfleri büyük harfle yazdıran bir Python programı yazın. Örneğin, 'merhaba' için 'mErhAbA' yazmalıdır.",
    "33- Bir dizideki tüm elemanların karelerini hesaplayarak yeni bir liste oluşturan bir Python programı yazın. Örneğin, [1, 2, 3] için [1, 4, 9] yazmalıdır.",
    "34- Kullanıcıdan bir dizi sayı alıp, bu sayıları en büyükten küçüğe sıralayan bir Python programı yazın. Örneğin, [4, 2, 3, 1] için [4, 3, 2, 1] yazmalıdır.",
    "35- Bir dizideki sayıları pozitif hale getiren bir Python programı yazın. Örneğin, [-1, -2, 3] için [1, 2, 3] yazmalıdır.",
    "36- Kullanıcıdan bir dizi sayı alıp, bu sayılardaki en küçük ve en büyük sayıyı bulan bir Python programı yazın. Örneğin, [5, 1, 7, 3] için 1 ve 7 yazmalıdır.",
    "37- Kullanıcıdan bir dizi sayı alıp, bu sayıların ortalamasını hesaplayan bir Python programı yazın. Örneğin, [1, 2, 3] için ortalama 2 yazmalıdır.",
    "38- Kullanıcıdan bir dizi alıp, bu dizideki elemanların kaç kez tekrarlandığını bulan bir Python programı yazın. Örneğin, [1, 1, 2, 3] için 1:2, 2:1, 3:1 yazmalıdır.",
    "39- Kullanıcıdan bir metin alıp, bu metindeki sesli harfleri bulan bir Python programı yazın. Örneğin, 'Python' için 'o' yazmalıdır.",
    "40- Kullanıcıdan bir sayı alıp, bu sayının 5 ile tam bölünüp bölünmediğini kontrol eden bir Python programı yazın. Örneğin, 10 için 'evet' yazmalı.",
    "41- Bir dizideki tek sayıların toplamını bulan bir Python programı yazın. Örneğin, [1, 2, 3, 4] için 4 yazmalıdır.",
    "42- Kullanıcıdan bir kelime alıp, bu kelimenin içinde 'e' harfi olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 'merhaba' için 'var' yazmalıdır.",
    "43- Kullanıcıdan bir metin alıp, bu metindeki her kelimenin son harfini büyük harfle yazdıran bir Python programı yazın. Örneğin, 'ben program yazıyorum' için 'beN prograM yazıyoruM' yazmalıdır.",
    "44- Kullanıcıdan bir sayı alıp, bu sayının 10 ile 20 arasında olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 15 için 'evet' yazmalı.",
    "45- Kullanıcıdan bir dizi sayı alıp, bu sayılardaki en büyük sayının kaçıncı eleman olduğunu bulan bir Python programı yazın. Örneğin, [1, 3, 2] için 1 yazmalıdır.",
    "46- Bir dizideki tüm sayıları 2 katına çıkaran bir Python programı yazın. Örneğin, [1, 2, 3] için [2, 4, 6] yazmalıdır.",
    "47- Kullanıcıdan bir metin alıp, bu metindeki her kelimenin uzunluğunu yazdıran bir Python programı yazın. Örneğin, 'ben program yazıyorum' için 3, 6, 9 yazmalıdır.",
    "48- Kullanıcıdan bir metin alıp, bu metindeki büyük harflerin sayısını bulan bir Python programı yazın. Örneğin, 'Ben Program Yazıyorum' için 3 yazmalıdır.",
    "49- Kullanıcıdan bir sayı alıp, bu sayının 100 ile 200 arasında olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 150 için 'evet' yazmalı.",
    "50- Kullanıcıdan bir metin alıp, bu metindeki tüm kelimeleri ters çeviren bir Python programı yazın. Örneğin, 'ben program yazıyorum' için 'neb margorp muzyoray' yazmalıdır.",
    "51- Kullanıcıdan bir metin alıp, bu metindeki 'Python' kelimesinin kaç kez geçtiğini bulan bir Python programı yazın. Örneğin, 'Python Python' için 2 yazmalıdır.",
    "52- Kullanıcıdan bir dizi sayı alıp, bu sayılardaki en küçük sayının kaçıncı eleman olduğunu bulan bir Python programı yazın. Örneğin, [1, 3, 2] için 0 yazmalıdır.",
    "53- Bir dizideki tüm elemanları bir listeye ekleyen bir Python programı yazın. Örneğin, [1, 2, 3] için [1, 2, 3] yazmalıdır.",
    "54- Kullanıcıdan bir sayı alıp, bu sayının 3 ile tam bölünüp bölünmediğini kontrol eden bir Python programı yazın. Örneğin, 9 için 'evet' yazmalı.",
    "55- Kullanıcıdan bir metin alıp, bu metindeki en sık geçen harfi bulan bir Python programı yazın. Örneğin, 'banana' için 'a' yazmalıdır.",
    "56- Kullanıcıdan bir sayı alıp, bu sayının pozitif veya negatif olduğunu kontrol eden bir Python programı yazın. Örneğin, -1 için 'negatif' yazmalı.",
    "57- Kullanıcıdan bir dizi alıp, bu dizideki en uzun kelimeyi bulan bir Python programı yazın. Örneğin, ['ben', 'program', 'yazıyorum'] için 'yazıyorum' yazmalıdır.",
    "58- Kullanıcıdan bir metin alıp, bu metindeki tüm büyük harfleri küçük harfle yazdıran bir Python programı yazın. Örneğin, 'MERHABA' için 'merhaba' yazmalıdır.",
    "59- Kullanıcıdan bir metin alıp, bu metindeki tüm sayıları bulup toplayan bir Python programı yazın. Örneğin, 'ben 2 elma, 3 armut aldım' için 5 yazmalıdır.",
    "60- Kullanıcıdan bir sayı alıp, bu sayının 7 ile tam bölünüp bölünmediğini kontrol eden bir Python programı yazın. Örneğin, 14 için 'evet' yazmalı.",
    "61- Kullanıcıdan bir kelime alıp, bu kelimenin içinde 'i' harfi olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 'merhaba' için 'yok' yazmalıdır.",
    "62- Kullanıcıdan bir metin alıp, bu metindeki tüm sesli harfleri sayan bir Python programı yazın. Örneğin, 'merhaba' için 3 yazmalıdır.",
    "63- Kullanıcıdan bir sayı alıp, bu sayının karesini ve küpünü hesaplayan bir Python programı yazın. Örneğin, 2 için 4 ve 8 yazmalıdır.",
    "64- Bir dizideki tüm elemanları birbirleriyle çarpan bir Python programı yazın. Örneğin, [1, 2, 3] için 6 yazmalıdır.",
    "65- Kullanıcıdan bir kelime alıp, bu kelimenin uzunluğunu bulan bir Python programı yazın. Örneğin, 'merhaba' için 7 yazmalıdır.",
    "66- Kullanıcıdan bir metin alıp, bu metindeki kelimeleri alfabetik sıraya koyan bir Python programı yazın. Örneğin, 'kedi ayı' için 'ayı kedi' yazmalıdır.",
    "67- Kullanıcıdan bir sayı alıp, bu sayının 2'nin katı olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 8 için 'evet' yazmalı.",
    "68- Kullanıcıdan bir sayı alıp, bu sayıyı tersten yazdıran bir Python programı yazın. Örneğin, 123 için 321 yazmalıdır.",
    "69- Bir dizideki tüm sayıları toplayarak yeni bir liste oluşturan bir Python programı yazın. Örneğin, [1, 2, 3] için [1, 3, 6] yazmalıdır.",
    "70- Kullanıcıdan bir metin alıp, bu metindeki tüm 'a' harflerini kaldıran bir Python programı yazın. Örneğin, 'merhaba' için 'merhb' yazmalıdır.",
    "71- Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir Python programı yazın. Örneğin, 4! = 24 olmalıdır.",
    "72- Kullanıcıdan bir metin alıp, bu metindeki harflerin sırasını değiştiren bir Python programı yazın. Örneğin, 'merhaba' için 'baharem' yazmalıdır.",
    "73- Kullanıcıdan bir dizi alıp, bu dizideki elemanların kaç kez tekrarlandığını bulan bir Python programı yazın. Örneğin, [1, 1, 2, 3] için 1:2, 2:1, 3:1 yazmalıdır.",
    "74- Kullanıcıdan bir kelime alıp, bu kelimenin içinde 'o' harfi olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 'merhaba' için 'yok' yazmalıdır.",
    "75- Kullanıcıdan bir metin alıp, bu metindeki en sık geçen kelimeyi bulan bir Python programı yazın. Örneğin, 'ben ben ben' için 'ben' yazmalıdır.",
    "76- Kullanıcıdan bir sayı alıp, bu sayının 5 ile tam bölünüp bölünmediğini kontrol eden bir Python programı yazın. Örneğin, 10 için 'evet' yazmalı.",
    "77- Kullanıcıdan bir metin alıp, bu metindeki tüm harfleri küçük harfe çeviren bir Python programı yazın. Örneğin, 'MERHABA' için 'merhaba' yazmalıdır.",
    "78- Bir dizideki tüm sayıları bir listeye ekleyen bir Python programı yazın. Örneğin, [1, 2, 3] için [1, 2, 3] yazmalıdır.",
    "79- Kullanıcıdan bir sayı alıp, bu sayının 3 ile tam bölünüp bölünmediğini kontrol eden bir Python programı yazın. Örneğin, 9 için 'evet' yazmalı.",
    "80- Kullanıcıdan bir kelime alıp, bu kelimenin içinde 'e' harfi olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 'merhaba' için 'var' yazmalıdır.",
    "81- Kullanıcıdan bir metin alıp, bu metindeki tüm sesli harfleri sayan bir Python programı yazın. Örneğin, 'merhaba' için 3 yazmalıdır.",
    "82- Kullanıcıdan bir sayı alıp, bu sayının karesini ve küpünü hesaplayan bir Python programı yazın. Örneğin, 2 için 4 ve 8 yazmalıdır.",
    "83- Bir dizideki tüm elemanları toplayarak yeni bir liste oluşturan bir Python programı yazın. Örneğin, [1, 2, 3] için [1, 3, 6] yazmalıdır.",
    "84- Kullanıcıdan bir kelime alıp, bu kelimenin uzunluğunu bulan bir Python programı yazın. Örneğin, 'merhaba' için 7 yazmalıdır.",
    "85- Kullanıcıdan bir metin alıp, bu metindeki kelimeleri alfabetik sıraya koyan bir Python programı yazın. Örneğin, 'kedi ayı' için 'ayı kedi' yazmalıdır.",
    "86- Kullanıcıdan bir sayı alıp, bu sayının 2'nin katı olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 8 için 'evet' yazmalı.",
    "87- Kullanıcıdan bir sayı alıp, bu sayıyı tersten yazdıran bir Python programı yazın. Örneğin, 123 için 321 yazmalıdır.",
    "88- Bir dizideki tüm sayıları toplayarak yeni bir liste oluşturan bir Python programı yazın. Örneğin, [1, 2, 3] için [1, 3, 6] yazmalıdır.",
    "89- Kullanıcıdan bir metin alıp, bu metindeki tüm 'a' harflerini kaldıran bir Python programı yazın. Örneğin, 'merhaba' için 'merhb' yazmalıdır.",
    "90- Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir Python programı yazın. Örneğin, 4! = 24 olmalıdır.",
    "91- Kullanıcıdan bir metin alıp, bu metindeki harflerin sırasını değiştiren bir Python programı yazın. Örneğin, 'merhaba' için 'baharem' yazmalıdır.",
    "92- Kullanıcıdan bir dizi alıp, bu dizideki elemanların kaç kez tekrarlandığını bulan bir Python programı yazın. Örneğin, [1, 1, 2, 3] için 1:2, 2:1, 3:1 yazmalıdır.",
    "93- Kullanıcıdan bir kelime alıp, bu kelimenin içinde 'o' harfi olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 'merhaba' için 'yok' yazmalıdır.",
    "94- Kullanıcıdan bir metin alıp, bu metindeki en sık geçen kelimeyi bulan bir Python programı yazın. Örneğin, 'ben ben ben' için 'ben' yazmalıdır.",
    "95- Kullanıcıdan bir sayı alıp, bu sayının 5 ile tam bölünüp bölünmediğini kontrol eden bir Python programı yazın. Örneğin, 10 için 'evet' yazmalı.",
    "96- Kullanıcıdan bir metin alıp, bu metindeki tüm harfleri küçük harfe çeviren bir Python programı yazın. Örneğin, 'MERHABA' için 'merhaba' yazmalıdır.",
    "97- Bir dizideki tüm sayıları bir listeye ekleyen bir Python programı yazın. Örneğin, [1, 2, 3] için [1, 2, 3] yazmalıdır.",
    "98- Kullanıcıdan bir sayı alıp, bu sayının 3 ile tam bölünüp bölünmediğini kontrol eden bir Python programı yazın. Örneğin, 9 için 'evet' yazmalı.",
    "99- Kullanıcıdan bir kelime alıp, bu kelimenin içinde 'e' harfi olup olmadığını kontrol eden bir Python programı yazın. Örneğin, 'merhaba' için 'var' yazmalıdır.",
    "100- Kullanıcıdan bir metin alıp, bu metindeki tüm sesli harfleri sayan bir Python programı yazın. Örneğin, 'merhaba' için 3 yazmalıdır."
]

# Toplam klasör sayısı
total_examples = len(problems)

# Klasör ve dosya isimlerini oluşturacak olan döngü
for i in range(total_examples):
    # Her örnek için klasör ismi
    folder_name = f"example_{i + 1:03}"  # Örneğin, "example_001", "example_002" şeklinde numaralandırma
    
    # Klasörü oluştur
    os.makedirs(folder_name, exist_ok=True)
    
    # .txt ve .py dosyalarını oluştur
    problem_file = os.path.join(folder_name, f"example_{i + 1:03}_problem.txt")
    solution_file = os.path.join(folder_name, f"example_{i + 1:03}_solution.py")
    
    # Problemi dosyaya yaz
    with open(problem_file, 'w', encoding='utf-8') as f:  # UTF-8 kodlaması ile aç
        f.write(problems[i])  # Problemi dosyaya yaz
    
    # Boş çözüm dosyasını oluştur
    with open(solution_file, 'w', encoding='utf-8') as f:  # UTF-8 kodlaması ile aç
        pass

print(f"{total_examples} adet klasör ve dosya oluşturuldu.")
