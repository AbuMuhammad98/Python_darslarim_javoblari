def mango(quantity, price):
    while True:
        total = quantity * price
        if quantity < 3:
            total = quantity * price
        elif 2 < quantity < 6:
            total = (quantity // 3 * 2 + quantity % 3) * price
        elif quantity > 5:
            price = 5
            total = (quantity // 3 * 2 + quantity % 3) * price
        return total
print(mango(3600, 5))
# 3600 should equal 10136