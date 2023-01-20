# Raqamlar yigindisi
raqam = int(input("Raqamni kiriting: "))
son = 0
while raqam != 0:
    p = raqam %10
    son += p
    raqam //=10
print(son)