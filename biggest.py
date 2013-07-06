def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big = 0
    biggestkey = []
    if len(aDict.values()) == 0:
         return None
    for key, value in aDict.iteritems():
         if len(value) >= big:
             print (value, len(value),key)
             big = len(value)
             print big
             biggestkey.insert(0,key)
    return biggestkey[0]
