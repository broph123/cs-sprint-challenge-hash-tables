def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # My Hashtable
    posNeg = {}
    solution = []

    for num in a:
        if num > 0:
            posNeg[num] = True

    for num in a:
        if num < 0 and abs(num) in posNeg:
            solution.append(abs(num))

    return solution


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
