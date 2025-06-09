"""

TODOS LOS EJERCICIOS SE HAN PROBADO EN https://www.online-python.com/
Rafael Alpañez Vega
Prometeo FP (Máster thePower)

Basado en documentación oficial, foros técnicos y material educativo

"""

# EJERCICIO 1
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

miCadena = "Me encanta la programación" # definimos una variable de tipo string

def frecLetras(cadena): # Creamos la funcion
    cadena = cadena.lower() # pasaré todo a minúsculas para que ignore mayúsculas/minúsculas
    diccionario = {} # creo el diccionario
    for letra in cadena: #bucle for: recorre el string, detecta espacios, cuenta letras
        if letra != " ":
            diccionario[letra] = diccionario.get(letra, 0) + 1
    return diccionario

# llamamos a la función para probarla
print(frecLetras(miCadena))
# FIN EJERCICIO 1


# EJERCICIO 2
# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

listaNumeros = [1, 5, 10, 20, 60] # creamos lista de numeros
resultadoNumeros = list(map(lambda x: x * 2, listaNumeros))
# list convertirá el resultado en lista que es lo que nos piden
# nos piden usar map, (de ahi el anterior list, por el resultado), pero nos sirve para aplicar una funcion 'x' a cada elemento
# lambda nos crea una función pequeña sin necesidad de definira, en este caso duplicaremos el valor de entrada
print(resultadoNumeros) # imprimimos el resultado
# FIN EJERCICIO 2


# EJERCICIO 3
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

listaPelis = [
    "Harry Potter y la piedra filosofal",
    "El señor de los anillos: La comunidad del anillo",
    "Harry Potter y la cámara secreta",
    "El padrino",
    "Harry el sucio",
    "Titanic",
    "Pottermanía",
    "Matrix"
] # la lista se la pedí a la IA, solo que generase una lista compatible con el ejercicio

palabraObjetivo = "Harry" # podríamos pasarla también directamente en la propia funcion

def buscarPalabra(lista, objetivo): # definimos funcion
    resultado = [] # el resultado de nuestra funcion ira aqui
    for cadena in lista: # recorremos la lista, cadena a cadena
        if objetivo in cadena: # si nuestra palabra objetivo está en esa cadena
            resultado.append(cadena) # añadimos la cadena al resultado
    return resultado # devolvemos el resultado

print(buscarPalabra(listaPelis, palabraObjetivo)) # imprimimos el resultado
# FIN EJERCICIO 3

# EJERCICIO 4
# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

listaNum4 = [10, 20, 30, 40] # creamos dos listas
listaNum4_2 = [5, 12, 14, 18]

def buscarDiferencias(a, b):
    resultado = list(map(lambda x, y: x - y, a, b)) # me basé en el ejercicio 2 ya que la operacion es simple
    return resultado

print(buscarDiferencias(listaNum4, listaNum4_2))
# FIN EJERCICIO 4


# EJERCICIO 5
#  Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

lista5 = [1, 2, 4, 6, 8, 7, 3, 5, 9, 9, 3, 6, 8, 2, 4] 
nota_aprobado = 5

def calcularMedia(lista, nota_aprobado):
    estado = "" # variable para almacenar el estado
    media = sum(lista) / len(lista) #sum para sumar y len para obtener el length
    if media >= nota_aprobado: # sencillo el condicional
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado) # devolvemos en forma de tulpa

print(calcularMedia(lista5, nota_aprobado))
# FIN EJERCICIO 5


# EJERCICIO 6
# Escribe una función que calcule el factorial de un número de manera recursiva.

# me ha costado un poco entenderlo, pero lo saqué
def calFact (numero):
    if numero == 1: # evitamos que la funcion se repita infinitamente
        return 1
    else:
        return numero * calFact(numero-1) # el numero se multiplica factorialmente (numero * -1)

print(calFact(10))
# FIN EJERCICIO 6


# EJERCICIO 7
# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

listaTulpas = [(5, 6, 7, 8), ("Buenos", 88, "días")] # lista de tulpas

def convertString(lista):
    resultado = list(map(str, lista)) # convierte cada tulpa en string
    return resultado

print(convertString(listaTulpas))
#FIN EJERCICIO 7

# EJERCICIO 8
# Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

try:
    num1 = float(input("Introduce el primer número: ")) # input 1
    num2 = float(input("Introduce el segundo número: ")) # input 2
    resultado = num1/num2 # dividimos normal
    print("Resultado: ", resultado)
except ValueError: # excepto estemos dividiendo cosas que no son numeros
    print("Solo se permiten números")
except ZeroDivisionError: # excepto diviamos por cero
    print("No se puede dividir por cero")
# FIN EJERCICIO 8


# EJERCICIO 9
# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

listaMascotas = [
    "Perro",
    "Gato",
    "Mapache",
    "Loro",
    "Tortuga",
    "Tigre",
    "Conejo",
    "Cocodrilo",
    "Hámster",
    "Serpiente Pitón",
    "Pez",
    "Oso"
] # le pedí la lista a chatGPT

def excluirMascotas(lista):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"] # lista del enunciado
    resultado = list(filter(lambda mascota: mascota not in prohibidas, lista)) # hacemos una lista de las mascotas que NO estén en la lista de prohibidas
    return resultado

print(excluirMascotas(listaMascotas))

# FIN EJERCICIO 9


# EJERCICIO 10
#  Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

lista10 = [12, 15, 50, 33, 55, 80, 75] # lista de ejemplo

try:
    if len(lista10) == 0: # len = length
        raise Exception("La lista está vacía.") # el error que mostraremos si la lista estuviese vacía
    else:
        media = sum(lista10) / len(lista10) # la suma de la lista dividida por el length de la lista
        print("Media: ", media)
except Exception as e: # recogemos el error y lo mostramos en caso de excepcion
    print("Error: ", e)
# FIN EJERCICIO 10


# EJERCICIO 11
# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

try:
    edad = int(input("Introduce tu edad: ")) # input
    if edad < 0: # if, elif y else bastante sencillos
        raise Exception("La edad no puede ser menor que 0")
    elif edad > 120:
        raise Exception("La edad no puede ser mayor que 120")
    else:
        print("Tu edad es: ", edad)
except ValueError: # sacado del ejercicio de antes
    print("Solo se permiten números")
except Exception as e: # sacado del ejercicio de antes
    print("Error: ", e)
# FIN EJERCICIO 11


# EJERCICIO 12
# Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

def contarLetras(frase):
    resultado = list(map(lambda palabra: len(palabra), frase.split()))
    # usaremos frase.split para que nos separe la frase en palabras
    # map aplica lambda a cada palabra
    # len me dará el lengthç de cada palabra
    return resultado

print(contarLetras("Me gusta programar en Visual Studio Code"))
# FIN EJERCICIO 12


# EJERCICIO 13
# Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

def devolverLetras(conjunto):
    final = []
    for letra in conjunto: # hacemos un for del conjunto
        if letra not in final: # si la letra no está en el nuevo list se agrega (así omitimos las q ya están)
            final.append(letra)
    resultado = list(map(lambda letra: (letra.upper(), letra.lower()), final)) # creamos una lista de tulpa con dos letras: min y MAY
    return resultado

print(devolverLetras("asanderreblamar"))
# FIN EJERCICIO 13


# EJERCICIO 14
# Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

listaPalabras = [
    "manzana",
    "mesa",
    "camión",
    "coche",
    "murciélago",
    "avión",
    "montaña",
    "perro",
    "mariposa",
    "cereal"
] # le pido la lista a GPT

def retPalIni(lista, letra):
    resultado = list(filter(lambda palabra: palabra.startswith(letra), lista)) # palabra de lista empieza por letra
    return resultado

print (retPalIni(listaPalabras, "m"))
# FIN EJERCICIO 14


# EJERCICIO 15
# Crea una función lambda que sume 3 a cada número de una lista dada

lista15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ejercicio15 = list(map(lambda sumar: sumar + 3, lista15)) # lambda sumar: sumar + 3 para cada elemento 'sumar', le sumamos 3 valga la redundancia
print(ejercicio15)
# FIN EJERCICIO 15


# EJERCICIO 16
# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

cadena16 = "Esto es una cadena de texto"
nNumero = 3

def masLargoQue(cadena, num):
    resultado = list(filter(lambda palabra: len(palabra) > num, cadena.split())) # para cada palabra miramos long y añadimos al list la palabra mayor en long que nNumero
    return resultado

print(masLargoQue(cadena16, nNumero))
# FIN EJERCICIO 16


# EJERCICIO 17
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
from functools import reduce # importamos (tuve que mirar docs)

listaDigitos = [5, 6, 7, 8, 9]
# 'x' es el acumulador, 'y' el valor actual
# 'x * 10 + y' va formando el numero
resultado = reduce(lambda x, y: x * 10 + y, listaDigitos)
print(resultado)
# FIN EJERCICIO 17


# EJERCICIO 18
# Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

estudiantes = [
    {"nombre": "Laura", "edad": 20, "nota": 95},
    {"nombre": "Carlos", "edad": 22, "nota": 88},
    {"nombre": "Lucía", "edad": 21, "nota": 90},
    {"nombre": "Pedro", "edad": 23, "nota": 76},
    {"nombre": "Marta", "edad": 20, "nota": 77},
    {"nombre": "Juan", "edad": 24, "nota": 92}
] # le pedí la lista a GPT

filtroEstudiantes = list(filter(lambda estudiante: estudiante["nota"] >= 90, estudiantes)) # filtro sencillo
print(filtroEstudiantes)
# FIN EJERCICIO 18


# EJERCICIO 19
# Crea una función lambda que filtre los números impares de una lista dada.

lista19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtro19 = list(filter(lambda x: x % 2, lista19)) # devuelve true solo cuando x es impar
print(filtro19)
# FIN EJERCICIO 19


# EJERCICIO 20
# Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

listaMixta = [1, 2, 3, "Hola", "buenas", "tardes"]
filtro20 = list(filter(lambda elemento: isinstance(elemento, int), listaMixta)) # devuelve true si el elemento es int
print(filtro20)
# FIN EJERCICIO 20


# Crea una función que calcule el cubo de un número dado mediante una función lambda.
# Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
# Concatena una lista de palabras. Usa la función reduce().
# Calcula la diferencia total en los valores de una lista. Usa la función reduce().
# Crea una función que cuente el número de caracteres en una cadena de texto dada.
# Crea una función lambda que calcule el resto de la división entre dos números dados.
# Crea una función que calcule el promedio de una lista de números.
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
# Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.


# Crea la clase Arbol
# Define un árbol genérico con un tronco y ramas como atributos.
# Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
# Código a seguir:
# Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# Implementar el método quitar_rama para eliminar una rama en una posición específica.
# Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
# Caso de uso:
#         a. Crear un árbol.
#         b. Hacer crecer el tronco una unidad.
#         c. Añadir una nueva rama.
#         d. Hacer crecer todas las ramas una unidad.
#         e. Añadir dos nuevas ramas.
#         f. Retirar la rama situada en la posición 2.
#         g. Obtener información sobre el árbol.


# Crea la clase UsuarioBanco
# Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
# Código a seguir:
# Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
# Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
# Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
# Implementar agregar_dinero para aumentar el saldo del usuario.
# Caso de uso:
#         a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#         b. Agregar 20 unidades al saldo de Bob.
#         c. Transferir 80 unidades de Bob a Alicia.
#         d. Retirar 50 unidades del saldo de Alicia.


# Crea una función llamada procesar_texto
# Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
# Código a seguir:
# Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
# Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
# Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
# Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
# Caso de uso:
# Verificar el funcionamiento completo de procesar_texto.


# Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.


# Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
# Reglas:
#         0 - 69: insuficiente
#         70 - 79: bien
#         80 - 89: muy bien
#         90 - 100: excelente


# Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).


# Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
#     a. Solicitar al usuario el precio original de un artículo.
#     b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
#     c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
#     d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
#     e. Mostrar el precio final de la compra, considerando o no el descuento.
#     f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.