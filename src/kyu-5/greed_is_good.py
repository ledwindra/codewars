def score(dice=None):

    """
    Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a 
    throw according to these rules. You will always be given an array with five six-sided dice values.

    Three 1's => 1000 points
    Three 6's =>  600 points
    Three 5's =>  500 points
    Three 4's =>  400 points
    Three 3's =>  300 points
    Three 2's =>  200 points
    One   1   =>  100 points
    One   5   =>   50 point

    A single die can only be counted once in each roll. For example, a "5" can only count as part of a triplet 
    (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

    Examples:
    Throw       Score
    ---------   ------------------
    5 1 3 4 1   50 + 2 * 100 = 250
    1 1 1 3 1   1000 + 100 = 1100
    2 4 4 5 4   400 + 50 = 450
    """
    
    dice.sort()
    triplet = []
    score = []

    for i in range(3):
        if len(set(dice[i : (i + 3)])) == 1:
            triplet = triplet + dice[i : (i + 3)]

    triplet = triplet[ : 3]

    for i in range(1, 7):
        if dice.count(i) > 3 and dice[0] < dice[1]: 
            dice = dice[ : 2]
        elif dice.count(i) > 3 and dice[0] == dice[1]:
            dice = dice[-2 : ]
        else:
            pass

    if len(triplet) > 0:
        if triplet[0] == 1:
            score.append(int(str(triplet[0]) + '000'))
        else:
            score.append(int(str(triplet[0]) + '00'))

        for i in range(len(dice)):
            if dice[i] == 1:
                score.append(100)
            elif dice[i] == 5:
                score.append(50)
            else:
                pass
    else:
        for i in range(len(dice)):
            if dice[i] == 1:
                score.append(100)
            elif dice[i] == 5:
                score.append(50)
            else:
                pass

    return sum(score)

if __name__ == "__main__":
    score()    