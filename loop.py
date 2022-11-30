#the floor division // rounds the result down to the nearest whole number

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

liz = [2,4,6,9,10,15,17,23,22,24,30]
for num in liz:
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)