# def biography(ism, familiya, tugilgan_yili, tugilgan_joy, email=None, telefen_raqam=None):
#     yoshi = 2023 - tugilgan_yili  
#     malumotnoma = {'Ism':ism,
#                    'Familiya':familiya,
#                    "Tug'ilgan yili":tugilgan_yili,
#                    "Yoshi":yoshi,
#                    "Tug'ilgan joy":tugilgan_joy,
#                    "Email":email,
#                    "Telefon raqam":telefen_raqam}
#     return malumotnoma 
   
# foydalanuvchi = biography('Zafar', 'Yusupov', 1998, 'Toshloq', 'Qwerty@gmail.com', 330061000)
# print(foydalanuvchi)

# def biography(ism, familiya, tugilgan_yili, tugilgan_joy, email='', telefon_raqam=None):
#     yoshi = 2023 - tugilgan_yili  
#     malumotnoma = {'Ism':ism,
#                     'Familiya':familiya,
#                     "Tug'ilgan yili":tugilgan_yili,
#                     "Yoshi":yoshi,
#                     "Tug'ilgan joy":tugilgan_joy,
#                     "Email":email,
#                     "Telefon raqam":telefon_raqam}
#     return malumotnoma 
   
# foydalanuvchi = biography('Zafar', 'Yusupov', 1998, 'Toshloq', 'Qwerty@gmail.com', 330061000)

# def biography(ism, familiya, tugilgan_yili, tugilgan_joy, email='', telefon_raqam=None):
#     yoshi = 2023 - tugilgan_yili  
#     malumotnoma = {'Ism':ism,
#                     'Familiya':familiya,
#                     "Tug'ilgan yili":tugilgan_yili,
#                     "Yoshi":yoshi,
#                     "Tug'ilgan joy":tugilgan_joy,
#                     "Email":email,
#                     "Telefon raqam":telefon_raqam}
#     return malumotnoma 
   
# foydalanuvchi = biography('Zafar', 'Yusupov', 1998, 'Toshloq', 'Qwerty@gmail.com', 330061000)


# mijozlar = []

# while True:
#     print("\nQuyidagi ma'lumotlarni to'ldiring", end="")
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     tugilgan_yili = int(input("Tug'ilgan yilingizni kiriting: "))
#     yoshi = 2023 - tugilgan_yili
#     tugilgan_joy = input("Tugilgan joyingizni kiriting: ")
#     email = input("Emailingizni kiriting: ")
#     telefon_raqam = input("Telefon raqamini kiriting: ")
    
#     mijozlar.append(biography(ism, familiya, tugilgan_yili, tugilgan_joy, email, telefon_raqam))
    
#     keyingi_mijoz = input("Yana mijoz kiritasizmi. (ha/yo'q)") 
#     if keyingi_mijoz != 'ha':
#         break
# print(mijozlar)

# def kattasi(x, y, z):
#     """eng katta sonni aniqlash"""
#     max = x
#     if y>=max:
#         max = y
#     if z>=max:
#         max = z
#     return max

# a = kattasi(5, 6, 7)
# print(a)

# def aylana_info(r, pi=3.14):
#     aylana={
#         'radius':r,
#         'diametr':r*2,
#         'yuzi':pi*r**2
#         }
#     return aylana

# misol = aylana_info(5)
# print(misol)    

# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar


# a = tub_sonlar_top(1, 50)
# print(a)

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x ==0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1] + sonlar[x-2])
    return sonlar

print(fibonacci(50))

