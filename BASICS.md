# Fundamentos de Python

### Variables
Las variables se pueden reasignar.

<var_name> = <var_data>

#### Tipos de Datos
type(<my_var>)

- Strings <class 'str'>
  - + : concatenacion
  - format: 
    template = "hola mi nombre es {} y mi apellido es {}".format(name, surname)
    template = f"hola mi nombres es {name} y mi apellido es {surname}"

- Number <class 'int'> <class 'float'>
  - incremento: lives += 1
  - decremento: lives -= 1
  - notacion científica: e+n / e-n

- Boolean <class 'bool'> True / False
  - negacion: not True / not False / not <my_bool_var>

#### Transformacion de tipos de datos

- Coversion de Number a String:
  str(<my_number>) => string

- Coversion de String a Number:
  int(<my_string>) => number

### Operadores aritmeticos:
El orden de ejecucion de las operaciones es el siguiente:
1. Parentesis
2. Exponentes
3. multiplicacion
4. division
5. adicion
6. sustraccion

- + : suma / concatenacion
- - : resta
- * : multiplicacion / concatenacion por cantidad de veces
- / : division
- % : residuo [ ejemplo: 10 % 3 => 1]
- // : solo quedarse con el numero entero [ 10 // 3 => 3]
- ** : exponencial [ 2 ** 3 => 8 ]

### Operadores de comparacion

- < Menor y > Mayor
- <= Menor o igual y >= Mayor o igual
- == igualacion
- != distinto

#### Comparacion de flotantes

Los calculos entre flotantes por la aproximación en memoria y los metodos de calculo de python por la precision decimal suelen diferir de los resultados aproximados. Ejemplo:

  x = 3.3
  y = 1.1 + 2.2 # da resultado 3.300000003

  print(x == y) => False!

Para solucionar este error se puede pasar a string y eliminar la precision decimal. Aunque esta no es una forma matemática.

  y_str = format(y, ".2g")
  print(str(x) == y_str) => True

Para resolverlo de forma matemática:

  tolerancia = 0.00001
  print(abs(x - y) < tolerancia) => True (si el error es menor a mi tolerancia, entonces puedo decir que son iguales)

### Operadores logicos

- and : 
  True and True => True
  True and False => False
  False and True => False
  False and False => False
  5 < 10  and 10 > 2 => True
  5 < 10  and 10 < 2 => True

- or :
  True and True => True
  True and False => True
  False and True => True
  False and False => False
  5 < 10  and 10 < 2 => True
  5 > 10  and 10 < 2 => False

- not 
  not (True and True) => False
  not (True and False) => True
  not (False and True) => True
  not (False and False) => True
  not (True and True) => False
  not (True and False) => False
  not (False and True) => False
  not (False and False) => True

### Operadores condicionales

- if 
  if <condicion 1>:
    print("Caso verdadero condicion 1")
  elif <condicion 2>:
    print("Caso verdadero condicion 2")
  else:
    print("Caso falso")

### Funciones de String

- in : chequea si determinada cadena de caracteres es parte de otra cadena.
  text = "El sabe programar en Python"
  print("Javascript" in text) => False
  print("Python" in text) => True

- len : cantidad de caracteres en una cadena
  size = len("amor")
  print(size) => 4

- .upper() : pasa todo a mayuscula -> text.upper()

- .lower() : : pasa todo a minuscula -> text.lower()

- .count() : apariciones de una cadena dentro de otra cadena -> text.count('a')

- .swapcase() : intercambia mayuscula por minuscula y viceversa -> text.swapcase()

- .startswith() : verifica si una cadena comienza con determinada cadena -> text.startswith('El')

- .endswith() : verifica si una cadena termina con determinada cadena -> text.endswith('hon')

- .replace() : reemplaza determinada cadena por otra cadena -> text.replace('Python', 'Go')

- .capitalize() : Pone la primera letra de la cadena en mayuscula

- .title() : Pone la primera letra de cada palabra de la cadena en mayuscula

- .isdigit() : verifica si la cadena es un digito (un potencial numero) -> "342".isdigit() => True

### Indexacion y slicing

text = "Esta es mi nueva cadena"
print(text[1]) => "s"
print(text[0:5]) => "Esta "
print(text[0:10]) => "Esta es mi"
print(text[10:]) => "nueva cadena"
print(text[:]) => "Esta es mi nueva cadena"
print(text[16:22:1]) => "cadena" el ultimo valor me indica la cantidad de saltos caracter por caracter
print(text[16:22:2]) => "cdn"

### Listas
Una lista puede tener cualquier tipo de dato almacenado en su estructura. Aplica el indixado.

  numers = [1, 4, 6, 2]
  print(type(numbers)) => <class 'list'>
  print(numers[1]) => 4

- Se pueden actualizar los valores de las listas, quiere decir que son mutables:

  numbers[1] = 9
  print(numers[1]) => 9

- Tambien aplica el slicing:

  print(numbers[:3]) => [1, 9, 6]

- Tambien aplica el operador in:

  print(1 in numers) => True

#### Metodos de las listas

- Agregar elementos al final de la lista -> .append()

  numers.append(700)

- Insertar elementos en una posicion especifica de la lista. Desplaza los elementos de indice superior a la derecha -> .insert()

  numbers.insert(0, 500) -> el primer parametro es la posicion en la lista
  numbers.insert(2, 25) -> el primer parametro es la posicion en la lista

- Concatenacion de listas con el operador +
  
  tasks = ["task1", "task2", "task3"]
  new_list = numbers + tasks

- Obtener indice de un elemento. Utilizando este metodo podemos hacer un update -> .index()

  indice = tasks.index("task2") -> 1
  tasks[indice] = "tarea2 nueva"

- Remover un elemento -> .remove()

  tasks.remove("task1")

- Remover un elemento de la lista por su indice  -> .pop()

  tasks.pop(2) -> elimina "task3" si no mando parametro elimina el ultimo elemento

- Reversar una lista -> .reverse()

  tasks.reverse()

- Ordenar una lista -> .sort()

  numbers.sort() -> si no pongo parametro lo hace de menor a mayor. En caso de strings lo hace por orden alfabetico. En caso de datos mezclados no puede hacer el ordenamiento.

### Tuplas
Las tuplas son inmutables. No se podrán agregar elementos a ellas, modificar ni tampoco remover.

  tupla_number = (1, 2, 4, 5)
  tupla_string = ('javier', 'patricio', 'maria')

  print(type(tupla_number)) -> <class 'tuple'>
  print(type(tupla_string)) -> <class 'tuple'>

- Los metodos de indexacion son los mismos que para listas:

  tupla_number[1] => 2
  tupla_string.index('maria') -> 2

- Tambien funciona el metodo count:

  tupla_string.count('maria') -> 1

- Para crear una lista a partir de una tupla:

  list_string = list(tupla_string)
  type(list_string) -> <class 'list'>

- Tambien puedo crear tuplas a partir de listas:

  my_tuple = tuple(tupla_string)
  type(my_tuple) -> <class 'tuple'>

### Diccionarios
Cada key se relaciona con su valor.

  my_dict = {
    'nombre': 'Javier',
    'apellido': 'Pepe',
    'edad': 33,
    'casado': False
  }

- Cantidad de pares clave-valor -> len()

  my_dict.len() -> 4

- Consulta de un valor en base a su clave:

  print(my_dict['nombre']) -> 'Javier'
  print(my_dict['lalala']) -> ERROR!!!!
  print(my_dict.get('edad')) -> 33
  print(my_dict.get('nada')) -> None

- Verificar si existe una clave en un diccionario:

  print('apellido' in my_dict) True
  print('otraqueno' in my_dict) False

- Actualizacion del valor del diccionaro por su clave:

  my_dict['nombre'] = 'Carlos Javier'

- eliminar una clave de un diccionario -> del o pop

  del my_dict['casado'] -> elimina el par clave-valor
  my_dict.pop('casado')

- Obtener los items de un diccionario -> .items()

  my_dict.items() -> devuelve los pares clave-valor del diccionario como lista de tuplas

- Obtener las claves de un diccionario -> .keys()

  my_dict.keys() -> devuelve una lista con las claves del diccionario

- Obtener los valores de un diccionario -> .values()

  my_dict.values() -> retorna una lista de los valores del diccionario

### Ciclo While
Es muy importante la identacion para identificar el bloque. Su sintaxis es:

  while <condicion>:
    '''
    codigo del bloque
    '''

Ejemplo:

  counter = 0

  while counter < 10:
    counter += 1
    print(counter)

Ejemplo de ruptura del ciclo con la instruccion <break>. En este caso va a imprimir del 1 al 14:

  counter = 0

  while counter < 20:
    counter += 1
    if counter == 15:
      break
    print(counter)

Otro metodo de interrupcion del ciclo con <continue>. En este caso va a imprimir de 15 a 20:

  counter = 0

  while counter < 20:
    counter += 1
    if counter < 15:
      continue
    print(counter)

### Ciclo For
Su sintaxis es:

  for element in range(n): -> n = largo del rango o podria ser inicio y final
    print(element)

Ejemplo de iteracion de listas, tuplas y diccionarios:

  my_list = [24, 41, 56, 79, 84, 90]
  for element in my_list:
    print(element)

  my_tuple = ('javier', 'nicolas', 'patricio')
  for name in my_tuple:
    print(name)
  
  my_product = {
    'name': 'camisa',
    'price': 150,
    'stock': 33
  }

  for key in my_product:
    print(key) -> imprime las llaves [name, price, stock]
  
  for key, value in my_product.items():
    print(key, '=>', value)

### Sets (conjuntos)

- Se pueden modificar
- No tienen orden
- No permiten duplicados
- Pueden tener varios tipos de datos

Sintaxis:

  set_countries = {
    'col',
    'mex',
    'bol'
  }

  print(set_countries)
  print(type(set_countries)) -> <class 'set'>

  set_from_string = set('hola')
  print(set_from_string) -> {'o', 'l', 'h', 'a'}

#### Metodos de conjuntos

- len() -> tamaño
- in -> pertenencia
- agregar elementos -> .add()

  set_countries.add('pe')

- actualizar un conjunto -> .update({})

  set_countries.update({'ar','ec','pe'})

- remover un elemento. Si el elemento no existe tira un error y falla el programa -> .remove()

  set_countries.remove('col')

- remover un elemento. Si el elemento no existe no tira error -> .discard()

  set_countries.remove('ar')

- limpiar todo el conjunto -> .clear()

  set_countries.clear()

### Operaciones con conjuntos

- UNION

  set_a = {
    'col',
    'mex',
    'bol'
  }

  set_b = {
    'pe',
    'bol'
  }

  set_c = set_a.union(set_b)
  set_d = set_a | set_b

- INTERSECCION

  set_e = set_a.intersection(set_b)
  set_f = set_a & set_b

- DIFERENCIA

  set_g = set_a.difference(set_b) -> {'mex', 'col'}
  set_h = set_a - set_b -> {'mex', 'col'}

- DIFERENCIA SIMETRICA (UNION - INTERSECCION)

  set_i = set_a.symmetric_difference(set_b) -> {'pe', 'col', 'mex'}
  set_j = set_a ^ set_b -> {'pe', 'col', 'mex'}

### List Comprehension
Creamos una lista y agregamos un elemento por cada iteracion del ciclo for en una sintaxis simple.

  >> my_list = [element for element in range(n)]

Podemos agregar una condicion para agregar o no el elemento:

  my_list = []

  for i in range(1, 11):
    if i % 2 == 0:
      my_list.append(i * 2)

  print(my_list) -> [4, 8, 12, 16, 20]

  numbers = [element * 2 for element in range(1, 11) if element % 2 == 0]

  print(numbers) -> [4, 8, 12, 16, 20]

### Dictionary Comprehension
Muy similar a las listas:

  my_dict = {}

  for i in range(1, 11):
    my_dict[i] = i * 2

  print(my_dict)

  dict_comp = {i: i * 2 for i in range(1, 11)}
  print(dict_comp)

- Otro ejemplo:

  import random
  countries = ['col', 'mex', 'bol', 'pe']
  population = {country: random.randint(1, 100) for country in countries}
  print(population)

- Otro ejemplo utilizando dos listas y el metodo zip():

  users = ['javi', 'nico', 'santi']
  edades = [12, 34, 25]

  users_dict = {user: edad for user, edad in zip(users, edades)}
  print(users_dict)

- El uso de condicionales es similar al de las listas:

  import random
  countries = ['col', 'mex', 'bol', 'pe']
  population = {country: random.randint(1, 100) for country in countries}
  print(population)

  result = {pais: poblacion for pais, poblacion in population.items() if poblacion > 50}
  print(result)