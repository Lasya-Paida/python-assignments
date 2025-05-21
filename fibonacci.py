def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

num_terms = 10
sequence = [fibonacci(i) for i in range(num_terms)]
print("Fibonacci sequence: ", sequence)
