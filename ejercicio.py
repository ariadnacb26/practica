#Ejercicio 1 
#Calcular el factorial de un número
#Planteamiento: Crea una función que reciba un número entero no
#negativo como parámetro y devuelva su factorial. El factorial
#de un número n es el producto de todos los enteros positivos desde 
#1 hasta n (por ejemplo, 5! = 5 * 4 * 3 2   1 = 120). Asegúrate de 
#manejar el caso especial donde n = 0, que devuelve 1.

def calcular_factorial(numero):
    # Si el número es 0, el factorial siempre es 1
    if numero == 0:
        return 1

    resultado = 1
    # Se multilican todos los números desde 1 hasta el número
    for i in range(1, numero + 1):
        resultado = resultado * i

    return resultado

# Ejemplo: el factorial de 6 es 6*5*4*3*2*1 = 720
print(calcular_factorial(6))  # Muestra: 720


