# Logic exercise consisiting on telling wether we are sleeping or not according
# to the next rules:
# it is not a weekday (boolean)
# we're on vacation (boolean)


def sleep(weekday, vacation):
    if not weekday or vacation:
        return True
    return False
