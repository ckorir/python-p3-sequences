#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < length:
        # Add numbers to the sequence until its length is equal to the specified length
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]

        # Append the next number to the Fibonacci sequence
        fibonacci_sequence.append(next_number)
    print(fibonacci_sequence[:length])
    pass