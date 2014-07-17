import math


def _fibonacci_number_start_0(n=0):
    # Outside code uses 0->, this algorithm uses 1->
    # Outside expects 0 as first number
    # Map 0 -> 0, 1 -> 1, 2 -> 1, ..
    if n == 0:
        return 0

    p = (1 + math.sqrt(5)) / 2
    q = 1/p

    return int((p**n + q**n) / math.sqrt(5) + 0.5)


def _fibonacci_number_start_1(n=1):
    # Outside code uses 0->, this algorithm uses 1->
    # Outside expects 0 as first number
    # Map 0 -> 1, 1 -> 1, 2 -> 2, ..
    n += 1

    p = (1 + math.sqrt(5)) / 2
    q = 1/p

    return int((p**n + q**n) / math.sqrt(5) + 0.5)