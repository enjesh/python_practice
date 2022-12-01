def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

# Important to note
""" Use 4-space indentation, and no tabs.
Wrap lines so that they don't exceed 79 characters.
Use blank lines to separate functions and classes, and larger blocks of code inside functions.
When possible, put comments on a line of their own.
Use docstrings.
Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
Name your classes and functions consistently.
    Use UpperCamelCase for classes and lowercase_with_underscores for functions and methods
    Always use self as the name for the first method argument
Don't use fancy encodings if your code is meant to be used in international environments.
Don't use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.
"""