from src.near_xhundred import near_xhundred


# Konstants
FIVEHUNDRED = 5
NUMBER = 100
DIFFERENCE1 = 400
DIFFERENCE2 = 100


def test_near_xhundred_default():
    assert not near_xhundred(FIVEHUNDRED, NUMBER)


def test_near_xhundred_diff1():
    assert near_xhundred(FIVEHUNDRED, NUMBER, DIFFERENCE1)


def test_near_xhundred_diff2():
    assert not near_xhundred(FIVEHUNDRED, NUMBER, DIFFERENCE2)


def test_all():
    test_near_xhundred_default()
    test_near_xhundred_diff1()
    test_near_xhundred_diff2()
