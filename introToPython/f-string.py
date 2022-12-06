#  Formatted string literals (f strings)
year = 2016
event = 'Referendum'
print (f'Results of the {year} {event}')

#  str.format()
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print ('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

# Strings have two distinct representations str() and repr()
s = 'Hello, world.'
print(str(s))

print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))


import math
print(f'The value of pi is approximately {math.pi:.3f}.')


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


#  '!a' applies ascii(), '!s' applies str(), and '!r' applies repr()
animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')

print(f'My hovercraft is full of {animals!a}.')

print(f'My hovercraft is full of {animals!s}.')


# = specifier - expand an expression to the text of the expression = then the representation of the evaluated expression
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')


print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# A number in the brackets used to refer to the position of the object passed into the str.format() method.
print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))


# keyword arguments
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))


# Positional and keyword arguments combined
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# integers and their squares and cubes
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# The str.rjust() method right-justifies a string by padding it with spaces on the left.
#  str.zfill(), which pads a numeric string on the left with zeros.
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))




print('12'.zfill(5))

print('-3.14'.zfill(7))

print('3.14159265359'.zfill(5))


# Old string formatting
import math
print('The value of pi is approximately %5.3f.' % math.pi)



# mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased),
# and 'a' opens the file for appending; any data written to the file is automatically added to the end.
# 'r+' opens the file for both reading and writing.
# The mode argument is optional; 'r' will be assumed if it’s omitted
f = open('workfile', 'w', encoding="utf-8")
# with open('workfile', encoding="utf-8") as f:
#     read_data = f.read()

# We can check that the file has been automatically closed.
print(f.closed)

# f.read()



# for line in f:
#     print(line, end='')

f.write('This is a test\n')
f.write('This is another test\n')



value = ('the answer', 42)
s = str(value)  # convert the tuple to string
print(f.write(s))


f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

print(f.seek(5))      # Go to the 6th byte in the file

print(f.read(1))

print(f.seek(-3, 2))  # Go to the 3rd byte before the end

print(f.read(1))



# import json
# x = [1, 'simple', 'list']
# json.dumps(x)