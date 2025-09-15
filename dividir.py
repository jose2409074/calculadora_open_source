def dividir(num1, num2):
    """
    Divide dos números, manejando la división por cero.
    """
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    return num1 / num2