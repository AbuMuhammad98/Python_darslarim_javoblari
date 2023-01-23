# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 11:02:57 2023

@author: AbuMuhammad
"""

# def karra(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma
# print(karra(1,2,9,10,2))

def talaba(ism, familiya, **malumotlar):
    malumotlar['Ism']=ism
    malumotlar['Familiya']=familiya
    return malumotlar

talaba1 = talaba('Zafar', 'Yusupov', ty=1998, tj='Toshloq', malumoti='Tugallanmagan Oliy')
talaba2 = talaba('Muhammadaziz', 'Yusufjonov', ty='2002', tj='Toshloq')
print(talaba1)
print(talaba2)
