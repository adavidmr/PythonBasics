from src.diff import diff

# Constants
NUMBER1 = 50
NUMBER2 = 300
MULTIPLIER = 5


def diff_test_smaller_no_p():
    assert diff(NUMBER1, NUMBER2) == 250


def diff_test_smaller():
    assert diff(NUMBER1, NUMBER2, MULTIPLIER) == 250


def diff_test_bigger_no_p():
    assert diff(NUMBER2, NUMBER1) == 500


def diff_test_bigger():
    assert diff(NUMBER2, NUMBER1, MULTIPLIER) == 1250
