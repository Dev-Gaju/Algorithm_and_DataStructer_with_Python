def backTrack(weights, maxWeights, i, combs, comb):
    if maxWeights<0:
        return
    elif i==len(maxWeights):
        combs.append(comb.copy())
    else:
        comb.append(i)
        backTrack(weights, i+1, maxWeights-weights[i], comb, combs)
        comb.pop()
        backTrack(weights, i+1, maxWeights, comb, combs)

def get_combs(weights, maxweights):
    combs = []
    backTrack(weights, maxweights, 0, combs, [])
    return combs

print(get_combs([2,3,5,67,4,3,7,4,4,3],20 ))
