def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = {}
    solution = []
    for nums in a:
        if abs(nums) in result:
            result[nums] = True
            solution.append(result[nums])

    print(solution)


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
