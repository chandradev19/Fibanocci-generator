def fibonacci_iterative(n):
    """
    Generates the first 'n' terms of the Fibonacci sequence iteratively.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            next_fib = fib_series[-1] + fib_series[-2]
            fib_series.append(next_fib)
        return fib_series

# Example usage:
num_terms = 10
print(f"Fibonacci series (iterative) up to {num_terms} terms: {fibonacci_iterative(num_terms)}"




