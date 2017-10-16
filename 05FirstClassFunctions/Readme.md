## First Class Functions

## Snippets

#### callable

The seven flavors of callable objects[i.e. `()` operator]:

+ User-defined functions: created with `def` statements or lambda expressions
+ Built-in functions: like `len` or `time.strftime`(implemented in C)
+ Built-in methods: methods implemented in C, like `dict.get`
+ Methods: functions defined in the body of a class.
+ Classes: when invoked, a class runs its `__new__` method to create an instance, then `__init__` to initialize it, and finally the instance is returned to the caller. Because there is no new operator in Python, calling a class is like calling a function
+ Class instances: if a class defines a `__call__` method, then its instances may be invoked as functions
+ Generator functions: functions or methods that use the `yield` keyword. When called, generator functions return a generator object.
