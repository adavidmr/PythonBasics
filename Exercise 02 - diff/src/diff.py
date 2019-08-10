# Differnece between two numbers.


def diff(n, m, p=2):    # by default p is 2
    if n <= m:
        return m - n
    else:
        return (n - m) * p
