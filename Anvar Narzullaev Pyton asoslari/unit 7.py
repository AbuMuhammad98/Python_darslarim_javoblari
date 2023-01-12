# ismlar = ["Ulug\'bek,", 'Shoxrux,', 'Fayzullo,']
# print(ismlar[0], 'bugun oshga borasanmi?')
# print(ismlar[1], 'kredit ola bildingmi?')
# print(ismlar[2], 'ishlaringiz qanday bo\'yapti?')
# pop() sugurib oladi.
# remove() 1 xhi qiymatni ochiradi
# insert() yangi qiymat beradi
# append() bu ham royxatga yangi qiymat qoshadi

sonlar = [1, 2, -6, 16, 0.5, 5.6, -9]
sonlar[1] = 95
sonlar.append(5555)
sonlar.remove(-6)
sonlar.insert(2, "bir")
del sonlar[0]
sonlar_1 = sonlar.pop(5)
t_shaxslar = ['Imom Buxoriy']
z_shaxslar = ['Abdullo domla']
a = t_shaxslar.pop()
b = z_shaxslar.pop()
print('Men tarixiy shaxslardan', a, 'bilan ko\'rishishni,', '\nzamonaviy shaxslardan', b, 'bilan ko\'rishishni istardim')