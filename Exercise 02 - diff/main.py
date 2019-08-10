from test.diff_test import diff_test_smaller
from test.diff_test import diff_test_smaller_no_p
from test.diff_test import diff_test_bigger_no_p
from test.diff_test import diff_test_bigger


if __name__ == "__main__":
    diff_test_smaller()
    diff_test_smaller_no_p()
    diff_test_bigger_no_p()
    diff_test_bigger()
    print("Everything passed")
