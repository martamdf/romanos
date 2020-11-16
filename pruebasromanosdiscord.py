simbolos = {
    'M':1000,
    'D':500,
    'C':100,
    'L':50,
    'X':10,
    'V':5,
    'I':1,
}

tipo1 = ['I', 'X' , 'C', 'M']
tipo5 = ['V', 'L', 'D']

valor_maximo = {
    1:11,
    5:8, 
    10:121,
    50:91,
    100:721,
    500:921,
    1000:4221,
} 

def romano_a_entero(romano):
    """
    Función que primero comprobará que los valores introducidos sean correctos.
    Si se introduce un 'int' o un valor no romano nos lanzará un error
    Esta misma, llama a la función 'de_simbolo_a_entero' y nos devuelve el proceso
    de transformar el romano introducido en un arabigo
    """
    l = []
    if isinstance(romano, int):
        raise ValueError(f"Parámetro {romano} debe ser un string")
    else:
        for letra in romano:
            if isinstance(letra, str) and letra.upper() in simbolos:
                l.append(letra.upper())
            elif isinstance(letra, str) and letra.isdigit():
                raise ValueError(f"Número {letra} no permitido")
            else:
                raise ValueError(f"Símbolo {letra} no permitido")
    l = de_simbolo_a_entero(l) 
    return l        

def de_simbolo_a_entero(romano):
    """
    Función, que primero, comprueba las repeticiones de los romanos tipo1 [I, X, C, M],
    comprueba las repeticiones de los romanos tipo5 [V, L, D].
    Después nos transforma el símbolo romano en una lista de valores.
    Dada la lista de valores comprobamos el valor máximo del numero romano.
    Una vez comprobemos el valor máximo pasamos a restarlos con la función 'restar'
    Y una vez restados, devolvemos la suma total de elementos que nos quedan.
    """
    lista_valores = []
    if not repeticiones_tipo1(romano): 
        raise ValueError("Hay mas de 3 repeticiones de tipo 1")
    if not repeticiones_tipo5(romano):
        raise ValueError("Hay mas de 2 repeticiones de tipo 5")

    for simbolo in romano: 
        valor = simbolos[simbolo]
        lista_valores.append(valor)
    if valor_maximo_num(lista_valores):
        raise ValueError("Elementos mal posicionados")
    lista_valores = restar(lista_valores) 
    return sum(lista_valores)

def repeticiones_tipo1(romano):
    """
    Función que comprueba que en el valor romano introducido no se repitan
    mas de 3 veces los simbolos tipo1 [I, X, C, M].
    En caso de que se repitan nos devolverá False.
    Si no se repiten, devuelve True
    """
    no_rep = True
    valor_anterior = ""
    contador = 0
    for letra in romano: 
        if letra in tipo1:
            if letra == valor_anterior:
                valor_anterior = letra  
                contador += 1
            else:
                valor_anterior = letra 
                contador = 0 
            if contador == 3:
                no_rep = False

    return no_rep

def repeticiones_tipo5(romano): 
    """
    Función que comprueba que en el valor romano introducido no se repitan
    mas de 1 vez los simbolos tipo5 [V, L, D].
    En caso de que se repitan nos devolverá False.
    Si no se repiten, devuelve True
    """
    no_rep = True
    valor_anterior = ""
    contador = 0
    for letra in romano:
        if letra in tipo5:
            if letra == valor_anterior:
                valor_anterior = letra
                contador += 1    
            else:
                valor_anterior = letra
                contador = 0
            if contador == 1:
                no_rep = False

    return no_rep

def valor_maximo_num(lista): # [1000, 1000, 100, 1000]
    """
    Función que comprobará el valor máximo que puede haber en el valor romano
    introducido, dado que:
    - Si el primer numero entroducido es:
        I El numero correcto de máximo valor será = IX = 9
        Y la suma de estos 2 valores romanos en arabigo seria = 1 + 10 = 11
        Si el primer valor romano es 'I', el valor máximo de ese
        valor romano total debe ser 11 (mirar dict 'valor_maximo') y nunca sobrepasará
        ese valor máximo
    Si se sobrepasa el valor máximo querrá decir que hemos posicionado mal los valores
    romanos y la funcion nos devolverá True
    En caso de que esté todo correcto, devuelve False
    """
    error = False
    val_max = valor_maximo[lista[0]]
    if sum(lista) > val_max:
        error = True
    return error

def restar(lista):
    """
    Función que comprobará una lista de valores arabigos que nosotros introduciremos
    una vez transformados los valores romanos en arabigos.
    Tenemos la condición del while len(lista) != 0, osea, que mientras que nos queden valores dentro 
    de la lista introducida seguirá operando.
    Teniendo 2 indices, primera_pos y segunda_pos, siempre comprobaremos el primer
    y el segundo valor.
    Si el primer valor es mayor o igual al segundo simplemente lo introduciremos en la lista
    vacía haciendo un .pop() de la lista introducida.
    Si el primer valor es menor que el segundo, introduciremos el resultado de la resta del .pop()
    del segundo valor (dado que es mayor que el primero) sobre el primero y el resultado lo añadiremos
    en la lista vacía.
    Dado el caso de que nos quedara un numero en la lista, quiere decir que len(lista) == 1
    por ejemplo en este romano [X C I] en valores_arabigos [10, 100, 1] lo que hacemos es que si la 
    longitud es == 1, simplemente hazme .pop() del valor restante.
    Cuando no queden valores, simplemente saldrá del while y nos retornará la lista de valores
    Ej: 'MMMCM' [1000, 1000, 1000, 100, 1000] nos devolverá = [1000, 1000, 1000, 900]
    """
    l = []
    primera_pos = 0
    segunda_pos = 1
    while len(lista) != 0:
        if len(lista) == 1:
            l.append(lista.pop(primera_pos))
        else:
            if lista[primera_pos] >= lista[segunda_pos]:
                l.append(lista.pop(primera_pos))
            else:
                l.append(lista.pop(segunda_pos)-lista.pop(primera_pos))

    return l 

if __name__ == "__main__":
    print(romano_a_entero('VIII'))