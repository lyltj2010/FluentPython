"""
Transform a function into a single-dispatch generic function.

>>> merge([1, 2], [3, 4])
[1, 2, 3, 4]
>>> merge((1, 2), (3, 4))
(1, 2, 3, 4)
>>> result = merge({"a": 1}, {"a": 2, "b": 3})
>>> result["a"]
2
>>> result["b"]
3
"""

from functools import singledispatch


@singledispatch
def merge(item1, item2):
    raise NotImplemented("Type Not support!")


@merge.register(list)
def _(list1, list2):
    result = list(list1)
    result.extend(list2)
    return result


@merge.register(tuple)
def _(tuple1, tuple2):
    result = tuple1 + tuple2
    return result


@merge.register(dict)
def _(dict1, dict2):
    result = {**dict1, **dict2}
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
