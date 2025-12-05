def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma.
    """
    return a + b

def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float): Minuendo.
        b (float): Sustraendo.

    Returns:
        float: Resultado de la resta.
    """
    return a - b

def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Producto de los números.
    """
    return a * b

def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float: Cociente de la división.

    Raises:
        ValueError: Si el divisor es cero.
    """
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        numeros (list[float]): Lista de números.

    Returns:
        float: Promedio de los números.

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    return sum(numeros) / len(numeros)
