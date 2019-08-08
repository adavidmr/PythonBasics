from src.sleep import sleep

def test_sleep_vacation_1():
    assert sleep(True, True) == True

def test_sleep_vacation_2():
    assert sleep(False, True) == True

def test_sleep_no_vacation_1():
    assert sleep(True, False) == False

def test_sleep_no_vacation_2():
    assert sleep(False, False) == True
