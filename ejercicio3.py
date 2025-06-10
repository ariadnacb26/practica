#Ejercicio 3: Calcular la suma de los dígitos de un número elevado a una potencia
#Planteamiento: Crea una función que reciba dos parámetros: un número entero positivo y un exponente.
# La función debe calcular el número elevado al exponente dado, luego sumar todos los dígitos del resultado y devolver esa suma.
# Por ejemplo, si el número es 2 y el exponente es 3, calcula  2^3 = 8, y la suma de los dígitos es 8.
# Si el número es 5 y el exponente es 2, calcula 5^2 = 25, y la suma de los dígitos es 2 + 5 = 7.

def sumar_digitos_potencia(base, exponente):
    resultado = base ** exponente  # Se eleva la base al exponente

    # Se convierte el resultado en texto y sumo cada número
    suma = 0
    for digito in str(resultado):
        suma = suma + int(digito)

    return suma

# Ejemplo: 6^3 = 216, 2 + 1 + 6 = 9
print(sumar_digitos_potencia(6, 3))  # Muestra: 9
