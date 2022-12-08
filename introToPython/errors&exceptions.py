# a colon (':') is missing before the print statement
# while True print('Hello world')

# ZeroDivisionError: division by zero
# 10 * (1/0)

# NameError: name 'spam' is not defined
# 4 + spam*3

# TypeError: can only concatenate str (not "int") to str
# '2' + 2

# One can write programs that handle selected exceptions
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         print(x)
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")



# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception instance
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                          # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)


# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise


# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()


# def this_fails():
#     x = 1/0

# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

# # Raising exceptions 
# raise NameError('HiThere')


# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise


# Exception Chaining
# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")


# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc


# Defining Clean-up Actions
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')


# def bool_return():
#     try:
#         return True
#     finally:
#         return False

# print(bool_return())


# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")

# divide(2, 1)


# divide(2, 0)


# divide("2", "1")


# Raising and Handling Multiple Unrelated Exceptions
# def f():
#     excs = [OSError('error 1'), SystemError('error 2')]
#     raise ExceptionGroup('there were problems', excs)

# f()


# Enriching Exceptions with Notes
# try:
#     raise TypeError('bad type')
# except Exception as e:
#     e.add_note('Add some information')
#     e.add_note('Add some more information')
#     raise


def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)








try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')