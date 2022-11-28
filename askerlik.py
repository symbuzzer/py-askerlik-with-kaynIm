cinsiyet=input("Cinsiyet giriniz (e/k): ")
if cinsiyet=="e":
    yas=input("Yaşınızı giriniz: ")
    if yas.isnumeric():
        if yas>="20":
            print("Askere gelmelisin")
        else:
            print("Erken")
    else:
        print("Lütfen yaş olarak bir sayı girin")
if cinsiyet=="k":
       print("MUAF")
if cinsiyet=="":
    print("Lütfen bir cinsiyet girin")
if cinsiyet!="e" and cinsiyet!="k" and cinsiyet!="":
    print("Cinsiyeti yanlış girdiniz")
input("Press Enter to continue...")
