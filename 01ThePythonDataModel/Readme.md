## The Python Data Model

> You can think of the Data Model as a description of Python as a **framework**. It formalizes the interfaces of the building blocks of the languages itself, such as sequences, iterators, functions, classes, context managers and so on.

## Snippets

How special methods are used?

> The first thing to know about special methods is that the are meant to be called by the Python interpreter, and not by you. You don't write `my_object.__len__()`. You write `len(my_object)` and if `my_object` is an instance of a user defined class, then Pyhton calls the `__len__` instance method you implemented.

Why `len` is not a method?

> `len` is not called as a method because it gets special treatment as part of the Python Data Model, just like `abs`. But thanks to the special method `__len__` you can also make `len` work with your own custom objects. This is fair compromise between the need for efficient built-in objects and the consistnecy of the language. Also from the Zen of Python: "Special cases aren't special enough to break the rules."
