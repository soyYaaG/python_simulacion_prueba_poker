def factorial(n: int) -> int:
    if n < 0:
        raise ValueError('Error no existe factorial de números negativos.')

    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def coeficiente_binomial(n: int, k: int) -> float:
    if k > n:
        raise ValueError('k no puede ser mayor a n.')

    return factorial(n) / (factorial((n - k)) * factorial(k))