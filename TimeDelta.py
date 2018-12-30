import datetime

def get_delta(pastTime):
    """
    :param pastTime:
    :return : the difference between 2 times

    """
    a = datetime.datetime.now()
    return a - pastTime