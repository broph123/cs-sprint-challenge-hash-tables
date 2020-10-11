def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # My Hashtable
    posNeg = {}
    solution = []

    for num in a:
        posNeg[num] = []

        if num in posNeg:
            solution.append(abs(num))


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
