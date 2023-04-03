import datetime
import pytz

# Checks if the list of grades has changed

def isUpdated(original, new):
    matching = True

    try:
        return_value = new.index([x for x in new if x not in original][0])
    except IndexError:
        matching = False

    return matching, return_value


def getTime():
    my_date = datetime.now(pytz.timezone('US/Central'))
    return my_date.strftime("%m/%d/%Y %I:%M:%S %p")