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

