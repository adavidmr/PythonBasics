# Konstants
HUNDRED = 100
DEFAULTDIFF = 10


def near_xhundred(xhundred, number, difference=DEFAULTDIFF):
    xhundred = xhundred * HUNDRED
    return (xhundred - number) <= difference
