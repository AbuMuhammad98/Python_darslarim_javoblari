# davlatlar = ['Angliya', 'Germaniya', 'AQSh', 'Fransiya', 'Russia']
# print('Davlatlar soni: ', len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)

# sonlar = list(range(120,1201))
# print(sonlar)
# jami = sum(sonlar)
# print('Ro\'yxatdagi sonlar yig\'indisi: ', jami)
# yuqori = max(sonlar)
# quyi = min(sonlar)
# print(yuqori - quyi)
# print(len(sonlar))
# print(sonlar[0:20])
# print(sonlar[-20:])

taomlar = ['Sut', 'Non', 'Asal', 'Go\'sht', 'Olmali kompot']
nonushta = taomlar[:]
# print(nonushta)
nonushta.remove('Go\'sht')
# print(nonushta)
nonushta.append('Kofe')
# print(nonushta)
nonushta.insert(0, 'Shakar')
# print(nonushta)
# print(taomlar)
nonushta[0] = "Qaymoq va non"
nonushta = tuple(nonushta)
print(nonushta)
nonushta[1] = "Bulochka"

