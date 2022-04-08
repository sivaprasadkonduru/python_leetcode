from functools import wraps
from time import time


def calc_time(fn):
    @wraps(fn)
    def time_diff(a, b):
        try:
            start_time = int(round(time() * 10000))
            return fn(a, b)
        finally:
            end_time = int(round(time() * 10000)) - start_time
            print(f"Total execution time of function: {fn.__name__} is : {end_time} ms"
            )

    return time_diff


@calc_time
def exec_loops(a, b):
    vals = [i for i in range(a, b) if i % 2 == 0]
    return vals

@calc_time
def add(a, b):
    return a + b


@calc_time
def sub(a, b):
    return a - b


@calc_time
def mul(a, b):
    return a * b


@calc_time
def div(a, b):
    return a / b


print(exec_loops(0, 20000))
