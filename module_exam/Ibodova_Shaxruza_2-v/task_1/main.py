""""""
"""
                                    iterable va iterator o'rtasidagi farq!
iterable -> list, tuple, set, dict, str
iterable -> iterator 
massiv = [ 1, 2, 3, 4, 5 ]
    iter = iter(massiv)
    item1 = next(iter)
iteratorni ishga tushurish uchun next bayonotidan foydalanamiz!    
"""


def my_filter(function, iterable):
    for item in iterable:
        if function(item):
            yield item


def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = my_filter(is_even, numbers)
print(list(even_numbers))
