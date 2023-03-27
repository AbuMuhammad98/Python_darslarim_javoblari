def square_digits(num):
    # Your code here
    return int(''.join([str(int(n)**2)for n in str(num)]))   