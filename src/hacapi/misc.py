import pytz
from datetime import datetime


# Checks if the list of grades has changed
def is_updated(original, new):
    matching = True

    try:
        return_value = new.index([x for x in new if x not in original][0])
    except IndexError:
        matching = False
        return_value = None

    return matching, return_value


def get_time():
    my_date = datetime.now(pytz.timezone('US/Central'))
    return my_date.strftime("%m/%d/%Y %I:%M:%S %p")
