from random import *

kullanim = []

kullanici_1 = input("Kullanıcı_1 adınızı giriniz: ")
kullanici_2 = input("Kullanıcı_2 adınızı giriniz: ")

if kullanici_1:
    devam_mi = int(input(kullanici_1 + " başlamak için 1'e basınız: "))
    sayi1 = randint(1, 11)

    while sayi1 < 21:
        if sayi1 < 21 and devam_mi == 1:
            print("Kartınız: ", sayi1)
            devam_mi = int(input("Devam etmek için 1'e, durmak için 2'ye basınız: "))
            if devam_mi == 1:
                sayi2 = randint(1, 11)
                sayi1 += sayi2

        if sayi1 > 21 and devam_mi == 1:
            print("Kartınız: ", sayi1)
            print("Bust! Kazanan: ", kullanici_2)
            exit()

        if sayi1 == 21 and devam_mi == 1:
            print("Kartınız: ", sayi1)
            print("Blackjack! Kazandınız!", kullanici_1)
            exit()


        if devam_mi != 1:
            print("Kartınız: ", sayi1)
            print("Sıranız bitti!")
            break


if kullanici_2:
    devam_mi = int(input(kullanici_2 + " başlamak için 1'e basınız: "))
    sayi1 = randint(1, 11)

    while sayi1 < 21:
        if sayi1 < 21 and devam_mi == 1:
            print("Kartınız: ", sayi1)
            devam_mi = int(input("Devam etmek için 1'e, durmak için 2'ye basınız: "))
            if devam_mi == 1:
                sayi2 = randint(1, 11)
                sayi1 += sayi2

        if sayi1 > 21 and devam_mi == 1:
            print("Kartınız: ", sayi1)
            print("Bust! Kazanan: ", kullanici_1)
            exit()

        if sayi1 == 21 and devam_mi == 1:
            print("Kartınız: ", sayi1)
            print("Blackjack! Kazandınız!", kullanici_2)
            exit()

        if devam_mi != 1:
            print("Kartınız: ", sayi1)
            print("Sıranız bitti!")
            break


if kullanici_1 > kullanici_2:
    print("Kazanan: ", kullanici_1)
elif kullanici_1 < kullanici_2:
    print("Kazanan: ", kullanici_2)
elif kullanici_1 == 21 and kullanici_2 == 21:
    print("Berabere!")
elif kullanici_1 == 21:
    print("Kazanan: ", kullanici_1)
elif kullanici_2 == 21:
    print("Kazanan: ", kullanici_2)
else:
    print("Berabere!")
