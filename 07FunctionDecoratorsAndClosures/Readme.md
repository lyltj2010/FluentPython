## Function decorators and closures

### Two crutial facts about decorators

+ Replace the decorated function with a different one.
+ Executed immediately when a module is loaded(import time)

### Import and Run time

> Function decorators are executed as soon as the module is imported(import time),
but the decorated functions only run when they are explicitly invoked(run time).

### Closures

When you care about closures?

> Closures only matter when you have nested functions.

What is closure?

> A closure is **a function** with an **extended scope** that encompasses non-global 
variables referenced in the body of the function but not defined there.

What is speical about closure?

> It does not matter whether the function is anonymous or not, what matters is that it 
can access non-global variables that are **defined outside of its body**!!!

### Typical Behavior

> It replaces the decorated function with a new function that accepts the same arguments and
usually returns whatever the decorated function was supported to return, while also doing some
extra processing.