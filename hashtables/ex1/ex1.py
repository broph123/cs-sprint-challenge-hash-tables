def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weightDict = {}
    limitSol = []

    for index, weight in enumerate(weights):
        weightDict[weight] = index

    for weight in weight:
        if weightDict == limit:
            limitSol.append(weightDict[weight])
            return limitSol
        else:
            return None
