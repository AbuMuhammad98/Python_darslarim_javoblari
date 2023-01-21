# def tugilgan_yil(ism, yosh):
#     """Tug'ilgan yilini hisoblash uchun"""
#     print(f"{ism} {2023 - yosh} - yil tug'ilgan")
    
# tugilgan_yil('Zafar', 25)

# def kv_kb(son):
#     """Sonning kvadrati va kubini huisoblash uchun"""
#     print(f"{son} ning kvadrati {son**2} ga, kubi esa {son**3} ga teng")
    
# kv_kb(3)   
    
# def juftmi(son):
#     """Juft yoki toqligini aniqlovchi funksiya"""
#     if son % 2:
#         print(f"{son} toq son")
#     else: print(f"{son} juft son")

# juftmi(8)


# def taqqoslash(x, y):
#     """Taqqoslash"""
#     if x > y:
#         print(f"{x} soni {y} sonidan katta")
#     elif x < y:
#         print(f"{y} soni {x} sonidan katta")
#     else:
#         print(f"{x} soni {y} soniga teng")
    
# taqqoslash(8, 8)


# def kvadrat(x, y=2):
#     """daraja"""
#     print(f"{x} ning {y} darajasi {x**y} ga teng")
    
# kvadrat(8, 9)
# kvadrat(8, 3)


def bolinish_alomati(son):
    """Bo'linish alomati"""
    for n in range(2, 11):
        if not son%n:
            print(f"{son} {n} soniga qoldiqsiz bo'linadi")
            
bolinish_alomati(9999449864652406546854065340653465340324105340653106541356456587987)