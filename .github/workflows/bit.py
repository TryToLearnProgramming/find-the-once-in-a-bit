#question-
'''Given a base-10 integer,n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary
 representation. solve using python'''

# Python program to find
# length of the longest
# consecutive 1s in
# binary reprsentation of
# a number.

def maxConsecutiveOnes(x):
    # Initialize result
    count = 0

    # Count the number of iterations to
    # reach x = 0.
    while (x != 0):
        # This operation reduces length
        # of every sequence of 1s by one.
        x = (x & (x << 1))

        count = count + 1

    return count


# Driver code
n = int(input())
print(maxConsecutiveOnes(n))
