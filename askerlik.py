import sys;

while True:
    cinsiyet=input("Cinsiyet giriniz (e/k): ")
    if cinsiyet=="e":
        while True:
            try:
                yas=int(input("Yaşınızı giriniz: "))
                if yas <= 20:
                    print("Erken")
                else:
                    print ("Askere gitmelisin")
                input("Çıkmak için Enter tuşuna basın...")
                sys.exit(0)
            except ValueError:
                print("Lütfen yaş olarak bir sayı girin")
                continue
    if cinsiyet=="k":
        print("MUAF")
        input("Çıkmak için Enter tuşuna basın...")
        sys.exit(0)
    if cinsiyet=="":
        print("Lütfen bir cinsiyet girin")
        continue
    if cinsiyet!="e" and cinsiyet!="k" and cinsiyet!="":
        print("Cinsiyeti yanlış girdiniz")
        continue
