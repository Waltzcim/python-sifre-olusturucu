import random
character = "abcdefghklmnopqrstuvwxyzABCGHKLMNOPQRSTUVWXYZ1234567890!#$&+-*"

uzunluk = int(input("Şifre kaç karakter olsun: "))

sayi = int(input("Kaç adet şifre olsun: "))

for x in range(0, sayi):
        password = ""
        for x in range(0, uzunluk):
            password_char = random.choice(character)
            password      = password + password_char
        print("Rastgele Oluşturulan Şifreniz : " , password)