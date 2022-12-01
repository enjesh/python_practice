def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# The default value is evaluated only once
i = 5

def f(arg=i):
    print(arg)

i = 6
f()



# This function accumulates the arguments passed to it on subsequent calls
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# If you don’t want the default to be shared between subsequent calls,
# you can write the function like this instead
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L