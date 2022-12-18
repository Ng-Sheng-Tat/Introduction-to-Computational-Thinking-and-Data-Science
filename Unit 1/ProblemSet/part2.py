# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:
    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # intialize final list of trips
    trips = []
    # create power list using helper function, and sort it - shortest first!
    power_list = sorted(get_partitions(cows), key = len)
    # Note that this returns a list of names (strings), and we will need to do
    # dictionary lookup later
    # Now time to filter the power list:
    possibilities = []
    for i in power_list:
        ship = []
        for j in i:
            ship_weights = []
            for k in j:
                ship_weights.append(cows[k])
                #print(ship_weights)
            ship.append(sum(ship_weights))
            #print(ship)
        if all(d <= limit for d in ship):
            possibilities.append(i)
    # possibiliies now contains some duplicates, which need to be removed
    pruned_possibilities = []
    for k in possibilities:
        if k not in pruned_possibilities:
            pruned_possibilities.append(k)
    # now find the minimum list length:
    min_list_len = min(map(len, pruned_possibilities))
    for l in pruned_possibilities:
        if len(l) == min_list_len:
            return l