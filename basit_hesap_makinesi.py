print("""************************
Hesap Makinesi Programı
      
İşlemler:
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
************************
""")

a=int(input("1. Sayı:"))
b=int(input("2. Sayı:"))

işlem=input("İşlemi giriniz:")

if işlem == "1":
    print("{} ile {} in toplamı {}'dir.".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} in farkı {}'dir.".format(a,b,a-b))
elif işlem == "3":
    print("{} ile {} in çarpımı {}'dir.".format(a,b,a*b))
elif işlem == "4":
    print("{} ile {} in bölümü {}'dir.".format(a,b,a/b))
else:
    print("Geçersiz İşlem.")