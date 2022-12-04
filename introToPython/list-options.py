fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))  # Find next banana starting at position 4

fruits.reverse()
print (fruits)

fruits.append('grape')
print (fruits)

fruits.sort()
print (fruits)

fruits.pop()

# Using lists as stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print (stack)

stack.pop()

print (stack)

stack.pop()

stack.pop()

print (stack)

# Using lists as Queues
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# queue.popleft()                 # The first to arrive now leaves

# queue.popleft()                 # The second to arrive now leaves

# print (queue)                   # Remaining queue in order of arrival

# List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)

print (squares)

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print (combs)


# Delete statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)


a = ['one', 'two', 3, 'four']
print(a)

a.append('seven')
print(a)

b = ['nine', 10, 'fifty', 'sixty']
a.append(b)
print(a)