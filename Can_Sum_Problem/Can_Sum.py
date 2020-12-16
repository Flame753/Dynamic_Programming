# Write a function 'cansum(targetSum, numbers)' that takes in a targetSum and and array of numbers as arguments.
# The function should return a boolean indicating whether or not it is possible to generate the targetSum using
# numbers from the array.
# You may use an element of the array as many times as needed.
# you may assume that all input numbers are non-negative.


def canSum(targetSum, numbers, memo=None):  # added a memo object
    if memo is None:
        memo = {}
    if targetSum in memo:  # add a base to return memo value
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True  # store return values into the memo
            return True
    memo[targetSum] = False # store return values into the memo
    return False
