#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0

    # Initialize the minimum operations and clipboard size
    min_ops = n  # At worst, you might have to paste n times
    clipboard = 1

    for i in range(2, n + 1):
        if n % i == 0:
            clipboard = i
            break

    # Calculate the number of operations
    while n > 1:
        if n % clipboard == 0:
            n //= clipboard
            min_ops += 1
        else:
            clipboard += 1
            min_ops += 2

    return min_ops
