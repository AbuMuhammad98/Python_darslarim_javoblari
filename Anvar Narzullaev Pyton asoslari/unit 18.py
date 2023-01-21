# savat =[]
# while True:
#     mahsulot = input("Savatga mahsulot qo'shing:")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
#     if javob != 'ha':
#         break


# e_bozor = {}
# n = 1
# while True:
#     mahsulot = input(f"{n}-mahsulotni kiriting: ")
#     narx = int(input(f"{mahsulot.title()} narxini kiriting: "))
#     n +=1
#     e_bozor[mahsulot] = narx
#     savol = input("Yana mahsuloq qo'shasizmi: (ha/yo'q) ")
#     if savol != "ha":
#         break
    
savat = ['olma', 'gilos', 'mashina', 'sut', 'samalyot', 'kompyuter', 'muzlatgich']
e_bozor = {'olma': '5000',
  'gilos': '10000',
  'uzum': '7000',
  'mashina': '5000$',
  'pech': '100$',
  'muzlatgich': '500$'}

while savat:
    kassa = savat.pop()
    if kassa in e_bozor.keys():
        narh = e_bozor[kassa]
        print(f"{kassa.title()} - {narh} ")
    else: print(f"Bizda {kassa} yo'q")
 
