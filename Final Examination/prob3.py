# Paste your code here
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    counter = 0
    for i in range(numTrials):
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        picks = []
        for j in range(3):
            k = random.choice(bucket)
            picks.append(k)
            bucket.remove(k)
        if picks[0] == picks[1] == picks[2]:
            counter += 1
    return counter/numTrials 