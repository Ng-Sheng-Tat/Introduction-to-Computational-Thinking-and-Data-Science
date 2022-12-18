# Paste your code here
def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    for i in range(1000):
        if test(i):
            return i
    for i in range(1000, -1000, -1):
        if test(i):
            return i
