def factorial(n):
    """Calculate the factorial of a natural number n."""
    if n < 0:
        return 'Only natural numbers!'
    if n < 2:
        return 1

    result = 1
    for x in range(2, n + 1):
        result = result * x

    return result


def factorial_recursive(n):
    """Calculate the factorial of a natural number n."""
    if n < 0:
        return 'Only natural numbers!'
    if n < 2:
        return 1

    return n * factorial_recursive(n - 1)
