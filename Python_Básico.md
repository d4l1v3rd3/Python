# Introducción a Python

Aprenderemos como funciona el scripting programando en Python. Nos centraremos o enfocaremos en seguridad, dandonos grandes skills. "Scripting for pentesters"

Aprenderemos:

- Variables
- Loops
- Functions
- Data Structures
- If statements
- Files

Usaremos el editor de codigo para resolver ejecercicios o retos. Aprenderemos lo básico para hacer scripts básicos.

Empezaremos instalando [Python](https://www.python.org/downloads/)

En programación, la sintaxis en muy importante, porque describe la escrutura de un buen lenguaje de programación. En términos simples, la sintaxis dice al ordenador como debe leer el codigo y esctructurar los simbolos, puntiación y palabras del lenguaje.

# Hello World

Vamos a crear una simple sintaxis de un programa

```
# Esto es un ejemplo de comentario
print("Hello world")
```

Como podemos ver en el anteiror codigo, solo hay dos lineas, cuándo ejecutamos el código vemos el output "Hello World". La línea 1 es un comentario y empieza con un "#" utilizado para ayudar a la gente que lee codigo.

Podemos controlar lo que sale en pantalla con "print()" dentro de unas ""

# Operaciones matematicas

Vamos a ver los operadores matematicos aplicados a python. Como si fuera una calculadora.

![image](https://github.com/user-attachments/assets/df4d62af-07b5-4888-a590-7d8e05c26b59)

Ahora que sabemos los operadores básicos, una gran parte que costruye python son los bucles y las reglas if "loops y if statements" Estos operadores evaluan condiciones en momentos particulares

![image](https://github.com/user-attachments/assets/07eef878-60c8-4cd2-b9cb-c7b4797f403f)

```
print(21 + 43)
print(142 - 52)
print(10 * 342)
print(5 ** 2)
```

# Variables y tipos de datos

Las variables se usan para guardar y actualizar datos de los programas del ordenador. Tenemos variables de nombre de datos.

```
comida = "ice cream"
dinero = 20000
```

Como vemos tenemos dos ejemplos "comida y dinero" cada uno guarda la variable "ice cream o 20000" 

Las variables son muy poderosas porque hacen cambios al programa. Siguiento los ejemplo podemos crear variables y que vayan cambiado o incrementando.

```
años = 30
años = años + 1
print(años)
```

Como vemos en la línea dos la variable "años" se actualiza, siempre se va a hacer caso a la ultima vez que se puso dicha variable y si al principio es 30 y luego + 1 pues 31

## Tipos de daots

- String : Usado para combinar caracteres, como letras o simbolos
- Integer: Numeros enteros
- Float: Numeros que pueden contener decimales o fracciones
- Boolean: Usado para datos para restringirlos en "true" o "false"
- List: Series de datos diferentes guardados en una colección

![image](https://github.com/user-attachments/assets/949a21b3-fde4-4d2e-beff-421832e9fdab)

# Operadores Logicos y Booleanos

Los operadores lógicos permiten realizar asignaciones y comparaciones y se utilizan en pruebas condicionales (como declaraciones if)

![image](https://github.com/user-attachments/assets/eb129f4c-38b7-4179-ab8c-c66eef6f35ad)

Los operadores booleanos se usan para conectar y comprara relaciones entre consultas. Como una declaración if, las condiciones son o "true o false"

![image](https://github.com/user-attachments/assets/05cb5f4a-4f76-4641-b602-6e9c39f5f1b6)

```
a = 1
if a == 1 or a > 10:
  print("a es igual a 1 o superior a 10")
```

```
nombre = "bob"
hambre = true
if nombre == "bob" and hambre == True:
    print("bob tiene hambre")
elif nombre == "bob" and not hungry:
    print("Bob no tiene hambre")
else : # Si todas las condiciones no son verdad
    print ("no esta seguro si tiene hambre o no")
```

# Introducción a las declaraciones IF

Usando estas declaraciones dejamos que el programa pueda tomar decisiones. El programa escoge la decisión basado en la condición. Un ejemplo abajo:

```
if age < 17;
    print("No eres mayor para conducir")
else:
    print("Eres mayor para conducir")
```

Componentes:

- If : Indica la declaración, basada en una condición "si tal cosa es esto pues esto"
- La condición : age < 17
- : Nos dice cuando acaba una condición o la declaración if
- else: cuando ninguna condición se cumple

![image](https://github.com/user-attachments/assets/f02d99aa-30c4-4950-bccb-4d157e7e63c3)

# Bucles

En programación, los bucles permiten que los programas iteren y realicen acciones varias veces, tenemos dos tipos de bucles, "for y while"

## Bucles While

Vamos a ver primero de toodo la estructura de un bucle while. Podemos hacer que el bucle sea indefinido o cuando la condición se cumpla.

```
i = 1
while 1 <=10:
  print(i)
  i = i + 1
```

Este bucle como vemos se repetira 10 veces, hasta que la variable llegue a iteración en cuestión.

- La variable i = 1
- La declaración while estepcifica cuando empieza y cuando acaba el bucle
- Cada vez hay un bucle, empieza con el anterior
- La siguiente linea hace que a variable i aumente su valor en 1

## Bucle For

Un bucle for se usa para iterar secuencias de una lista, las listas se usan para guardar objector dentro de una sola variable.

```
paginas = ["facebook.com", "google.com", "amazon.com"]
for site in paginas:
    print(site)
```

Este bucle se ejecuta 3 veces, listando toda la variable "paginas"

- La lista guarda 3 objetos
- El bucle itera cada elemento, y printea el elemento
- El programa para cuando el bucle termina y no quedan más elementos.

En python, tambien podemos hacer un rango de numeros usando la función "range". Un ejemplo de numeros 0-4. En programación siempre el número que se empieza es el 0, entonces contar 5 es 4 por que (0,1,2,3,4)

```
for i in range(5):
  print(i)
```

En caso de querer hacer del 0 a l 50

```
for i in range(51):
  print(i)
```

# Introducción a las funciones

Cuando un programa se hace mas grande y mas complejo, mucho codigo se repite, escribir el mismo codigo, aquí entran las funciones. Las funciones son bloques de codigo que llaman a diferentes lugares del programa.

Tenemos funciones que trabajan como una claculadora entre dos puntos, otro de distancia ente puntos, condiciones, etc.

```
def sayHello(name):
    print("Hola " + name + "! Encantado de conocerte")

sayHello("ben") # Output = Hola ben ! Encantado de conocerte.
```

- def : Indica el inicio de la funcion, dando el parametro de la funcion "name"
- Sigue el nomre de la función y un parentesis donde esta los avlores que pondremos ()
- : para cerrar

```
def calcCoste(item):
  if(item == "sweets"):
          return 3.99
  elif (item == "oranges"):
          return 1.99
  else:
          return 0.99

spent = 10
spent = spent + calcCoste("sweets")
print("tienes:" + str(spent))
```

Si llamamos a la funcion y ponemos el valor "sweets", la funcion devolvera el numero decimal. 


