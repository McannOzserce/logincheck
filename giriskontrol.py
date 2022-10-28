import functions




while (True) :
    kullaniciadi = input("Kullanıcı adı Giriniz : ")
    sifre = input("Sifre Girinz :")

    if functions.kullanicikontrol(kullaniciadi,sifre) == 1 :
        print("giris yapıldı Tebrikler")
        break
   
    else:
        print("giris yapılamadi Kullanıcı Adı veya Şifre Yanlış...")
        kayitkontrol = input("Kayıt olmak isterseniz 1 e istemezseniz 2 ye basınız : ")
        if kayitkontrol == "1" :

            while (True):

                yenikullaniciadi = input("Yeni kullanici adi giriniz :")
                yenisifre = input("Yeni şifre giriniz :")

                if functions.kayitkontrol(yenikullaniciadi,yenisifre) == 0 :
                    functions.userekle(yenikullaniciadi,yenisifre)
                    print("Başarıyla Kayıt Oldunuz")
                    break
                else:
                    print("kullanici adi daha önce kullanılmış Lütfen tekrar deneyiniz ")
        else:
            print("kayıt olmak istemediniz iyi günler diler tekrar bekleriz")
            break
            
                


 







