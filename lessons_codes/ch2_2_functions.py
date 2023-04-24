# from functools import reduce
from functools import wraps
from collections import OrderedDict
# from operator import add, mul


# Memoized decorator
def memoized(func):
    memo_dict = {}

    def inner(arg):
        nonlocal memo_dict
        if arg not in memo_dict:
            result = func(arg)
            memo_dict[arg] = result
            return result
        else:
            return memo_dict[arg]
    return inner


# @wraps (save the name of function, help etc.)
def wrapped(function):
    @wraps(function)
    def inner(arg):
        return function(arg)
    return inner


# Memoize of call_number of function
def memoizing(call_number):

    def wrapped(function):
        memo_dict = OrderedDict([])

        @wraps(function)
        def inner(arg):
            nonlocal memo_dict
            if arg not in memo_dict:
                result = function(arg)
                if len(memo_dict) == call_number:
                    memo_dict.popitem(last=False)
                memo_dict[arg] = result
                return result
            else:
                return memo_dict[arg]
        return inner
    return wrapped


# Composition of functions:
# def compose(f, g):
#     def inner(arg):
#         return f(g(arg))
#     return inner


# Линтер закономерно ругается на такие функции, потому что
# обычно именованные функции не делаются с помощью лямбд.
curry = lambda f: lambda x: lambda y: f(x, y)  # noqa: E731
compose = lambda f: lambda g: lambda x: f(g(x))  # noqa: E731
pair = lambda x: [x, x]  # noqa: E731
dup = lambda x: x + x  # noqa: E731
# f = curry(add)
# f(5)(6)
# 11
# add5 = curry(add)(5)
# add5(10)
# 15
# concat = curry(reduce)(add)
# concat(["Hello", ", ", "World!"])
# "Hello, World!"
