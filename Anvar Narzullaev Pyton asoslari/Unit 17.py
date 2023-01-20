# savol = "Sevgan kitobingini kiriting "
# savol += "(barcha kitoblarni kiritib bo'lgach 'Stop' deb yozing): "
# while True:
#     kitob = input(savol)
#     if kitob == 'stop':
#         break
# print("Rahmat")
        
# savol = "Yoshingizni kiriting: "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     if yosh < 7:
#         narx = 2000
#     elif 7 <= yosh < 18:
#         narx = 3000
#     elif 18 <= yosh < 65:
#         narx = 10000
#     else: narx = 0
    
#     if yosh == 0:
#         print('Sizga chipta bepul')
#     else:
#         print(f"Sizga chipta {narx} so'm")    

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if int(qiymat)<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")