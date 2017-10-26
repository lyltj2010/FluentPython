"""
Run this script, you will see something like this.

Runing register(<function f1 at 0x1048d78c8>)
Runing register(<function f2 at 0x1048d7950>)
Runing main()
registry -> [<function f1 at 0x1048d78c8>, <function f2 at 0x1048d7950>]
Runing f1()
Runing f2()
Runing f3()
"""

registry = []

def register(func):
    print("Runing register(%s)" % func)
    registry.append(func)
    return func

# Run right after the decorated function is defined
# At import time
# import this_file.py will trigger it
@register
def f1():
    print("Runing f1()")

# Just a syntactic sugar
# Same as
# f2 = register(f2)
@register
def f2():
    print("Runing f2()")

def f3():
    print("Runing f3()")

def main():
    # decorators run before this line
    print("Runing main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()