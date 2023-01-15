# izohli_lugat = {'integer':'butun son', 
#                 'float':'o\'nlik son', 
#                 'if':'agar', 
#                 'elif':'agar aks xolda', 
#                 'else':'aks xolda',
#                 'print':'chop etmoq',
#                 'string':'qator',
#                 'input':'foydalanuvchi tomonidan kiritiladigan ma\'lumot',
#                 'upper':'barcha harflarni kattada ko\'rsatish',
#                 'lower':'barcha harflarni kichikda ko\'rsatish',
#                 'title':'bosh harflarni kattada ko\'rsatish'
#                 }
# for k, v in izohli_lugat.items():
#     print(f"{k.title()} - {v.title()}")

# davlatlar = {'aqsh':'washington',
#               "fransiya":'paris',
#               'angliya':'london',
#               'uzbekistan':'tashkent',
#               'russia':'moskva',
#               }
# # print('Dunyo davlatlari: ')
# # for davlat in sorted(davlatlar):
# #     print(davlat.upper())


# # print('\nDavlatlarning poytaxtlari: ')
# # for poytaxt in sorted(davlatlar.values()):
# #     print(poytaxt.title())
    
# country = input("Davlatni kiriting: ").lower()
# capital = davlatlar.get(country)
# if capital == None:
#     print("Kechirasiz bunday davlat ro'yxatda yo'q")
# else:
#     print(f"{country.upper()} davlatining poytaxti {capital.title()}")


menu = {'osh':'25000',
         'kabob':'60000',
         'shurva':'20000',
         'manti':'28000',
         'somsa':'15000',
         'lagmon':'17000',
         'non':'5000',
         'salat':'10000',
         'kampot':'12000',
         'choy':'3000',
         }
print('3 ta taom buyurtma bering: ')
buyurtmalar= []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")