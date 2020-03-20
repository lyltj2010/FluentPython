## An Array of Sequences

Some generic operations on sequences.

#### Built-in Sequences

Container sequences:

> list, tuple and collections.deque can hold items of different types. 
> They hold references to the object they contain, which may be any types.

Flat sequences:

> str, bytes, bytearray, memoryview and array.array hold items of one type. 
> They physically store the value of each item within its own memory space, and not as distinct objects.

Mutable sequences:

> list, bytearray, array.array, collections.deque and memoryview

Immutable sequences:

> tuple, str and bytes
