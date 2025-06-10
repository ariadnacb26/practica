#Ejercicio 2
#Convertir un número decimal a binario
#Planteamiento: Escribe una función que reciba un número entero positivo y devuelva
#una cadena con su representación en binario (base 2). Por ejemplo, si se ingresa 10,
#la función debe devolver "1010". No uses funciones integradas de conversión a binario; 
#implementa la lógica dividiendo el número y construyendo la cadena manualmente.

def convertir_a_binario(numero_decimal):
    binario = ""

    # Se divide el número entre 2 hasta que llegue a 0
    while numero_decimal > 0:
        residuo = numero_decimal % 2  # Se saca el resto (0 o 1)
        binario = str(residuo) + binario  # Se agrega al principio del resultado
        numero_decimal = numero_decimal // 2  # Se divide entre 2 sin decimales

    # Si era 0, se devuelve "0"
    return binario if binario != "" else "0"

# Ejemplo: 20 en binario es 10100
print(convertir_a_binario(20))  # Muestra: "10100"