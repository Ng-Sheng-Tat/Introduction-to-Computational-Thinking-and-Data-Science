import math
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == []:
        return float("NaN")
    lenlist = []
    for ele in L:
        lenlist.append(len(ele))
    
    lenmean = sum(lenlist)/len(lenlist)
    sumcount = 0

    for ele in lenlist:
        sumcount += (ele - lenmean)**2
    
    returnans = math.sqrt(sumcount/len(L))

    return returnans

L = ['a', 'z', 'p']
print(stdDevOfLengths(L))