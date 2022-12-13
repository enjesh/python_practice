# import os
# print(os.getcwd())      # Return the current working directory

# print(os.chdir('C:\\Users\\User\\python-playground\\python_practice'))   # Change current working directory
# # print(os.system('mkdir today'))   # Run the command mkdir in the system shell


# import os
# print(dir(os))

# print(help(os))

# import shutil
# shutil.copyfile('data.db', 'archive.db')

# shutil.move('/build/executables', 'installdir')


# import glob
# glob.glob('*.py')

# import sys
# print(sys.argv)

# re module
# import re
# re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

# re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# 'tea for too'.replace('too', 'two')

# math module
import math
print(math.cos(math.pi / 4))

print(math.log(1024, 2))

# random module
import random
print(random.choice(['apple', 'pear', 'banana']))

print(random.sample(range(100), 10))   # sampling without replacement

print(random.random())    # random float

print(random.randrange(6))    # random integer chosen from range(6)

# statistics module
# import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.50, 1.25, 3.50]
# print(statistics.mean(data))

# print(statistics.median(data))

# print(statistics.variance(data))


# from urllib.request import urlopen
# with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
#     for line in response:
#         line = line.decode()             # Convert bytes to a str
#         if line.startswith('datetime'):
#             print(line.rstrip())         # Remove trailing newline



# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org

# Beware the Ides of March.
# """)
# server.quit()

# dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now)

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))


# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))


from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print(Timer('a,b = b,a', 'a=1; b=2').timeit())


# def average(values):
#     """Computes the arithmetic mean of a list of numbers.

#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)

# import doctest
# doctest.testmod()   # automatically validate the embedded tests


# import unittest

# class TestStatisticalFunctions(unittest.TestCase):

#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)

# unittest.main()  # Calling from the command line invokes all tests