import sys

# TTY stands for Teletypewriter and it accept input from a keyboard
# When commands are read from a tty, the interpreter is said to be in interactive mode

print(f'{sys.stdin.isatty()=}')
print(f'{sys.stdout.isatty()=}')
print(f'{sys.stderr.isatty()=}')

print(f' received input: {input ("enter your name: ")}')