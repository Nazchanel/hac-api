def isUpdated(original, new):
    matching = True

    try:
        return_value = new.index([x for x in new if x not in original][0])
    except IndexError:
        matching = False

    return matching, return_value
