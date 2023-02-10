"""
Xuqing Wu
CSE 163 AA

Below are three functions that deal with numbers and strings
each should be tested on the hw0_test file.
"""


def funky_sum(a: float, b: float, mix: float) -> float:
    """
    take three float parameters
    returns the weighted sum of first two floats
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def total(n: int) -> int | None:
    """
    take an inteher parameter n
    returns sum of the integers from 0 (inclusive) to n (inclusive)
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(source: str, c1: str, c2: str) -> str:
    """
    take three string parameters source, c1, c2
    all occurrences of c1 and c2 swapped
    returns a copy of source
    """
    source_copy = source
    for i in range(len(source)):
        if source_copy[i] == c1:
            source_copy = source_copy[0:i] + c2 + source_copy[1 + i:]
        elif source[i] == c2:
            source_copy = source_copy[0:i] + c1 + source_copy[1 + i:]
    return source_copy
