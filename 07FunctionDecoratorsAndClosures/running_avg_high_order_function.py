"""
Define a nested function.
How does the avg function find the series?
    * In the closure
    * Within averager, series is a free variable
    * Which means series is not bound in the local scope
Summarize closure
    * A closure is function that retains the bindings of free
    * variables that exist when the function is defined.
    * so they can be use later when the function is invoked and
    * the defining scope is no longer available
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0

# Inspecting compiled body of avg avg.__code__
>>> avg.__code__.co_varnames # local variable
('new_value', 'total')
>>> avg.__code__.co_freevars # free variable
('series',)

# Each free variable corresponds to one item in __closure__
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
"""

def make_averager():

    ### closure starts
    series = [] # free variable to averager

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    ### closure ends
    # return a callable
    return averager

if __name__ == "__main__":
    import doctest
    doctest.testmod()
