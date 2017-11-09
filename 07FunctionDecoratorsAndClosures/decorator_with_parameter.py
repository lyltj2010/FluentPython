"""
Use a decorator factory that takes arguments and returns a 
decorator, which is then applied to the function to be decorated.
>>> registry.pop().__name__
'f2'
"""

registry = set()

def register(active=True):
    def decorate(func):
        print("Running register(active=%s -> decorate(%s" % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


# will not be add to registry
@register(active=False) # return a decorator, which is callable
def f1():
    print("Running f1()")


# Same as f2 = register()(f2)
@register() # must be called even without parameter
def f2():
    print("Running f2()")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
