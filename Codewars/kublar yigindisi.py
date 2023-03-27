def sum_cubes(n):
    # your code here
  total = 0
  while n > 0:
    total += n ** 3
    n -= 1
  return total
print(sum_cubes(4))

# def sum_of_cubes(n):
#  total = 0
#  while n > 0:
#    total += n * n * n
#    n -= 1
#  return total
# print("Sum of cubes smaller than the specified number: ",sum_of_cubes(3))