def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weightDict = {}

    for i in range(len(weights)):
        weight = weights[i]
        comp = limit-weight
        if comp in weightDict:
            return [weightDict[comp], i]

        weightDict[weight] = i
    return None
