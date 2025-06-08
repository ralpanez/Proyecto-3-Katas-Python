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


# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().



# Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

# Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

# Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

# Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

# Crea una función lambda que sume 3 a cada número de una lista dada.

# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

# Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

# Crea una función lambda que filtre los números impares de una lista dada.

# Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
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