# # Raqamlar yigindisi
# raqam = int(input("Raqamni kiriting: "))
# son = 0
# while raqam != 0:
#     p = raqam %10
#     son += p
#     raqam //=10
# print(son)

chipta = int(input("Chipta raqamini kiriting: "))
ooo= 0
while chipta != 0:
  a = chipta % 10
  
  ooo+= a
  chipta //=1000
print(ooo)