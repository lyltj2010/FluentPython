"""
why len is not a method?
Practicality beats purity. Fast.
But __len__ also supported
Special cases aren't special enough to break the rules.
"""
lst = [1, 2, 3]
print(len(lst))
print(lst.__len__())
