import os
lista = []
user_input = input("Que deseas hacer?\n1. Agregar\n")
 
if user_input.lower() == "1":
    print("Preciona e para ejecutar el programa")
    
    while user_input.lower() != "e":
        user_input = input("Escribe un numero para ser agregado a la lista: ")
        try:
            if isinstance(int(user_input),int) : lista.append(int(user_input))
        except ValueError:
            if user_input != "e":
                print("El valor ingresado no es correcto")

def flatten(l):
    return [item for sublist in l for item in sublist]

def square(lst):
    squared = []
    for element in lst: 
        squared.append(element**3)
    return squared

if(len(lista) > 1):
    os.system('clear')
    splitted_list = [lista[:round(len(lista)/2)] , lista[round(len(lista)/2):]]
    print(f"Lista separada: {splitted_list}" )
    print( f"Primer elemento: {lista [0]} Ultimo elemento: {lista[-1]}" )
    lista.extend(flatten(splitted_list))
    print(f"Lista con elementos agregados: {lista}")
    lista.sort()
    print(f"Lista odenada asc: {lista}")
    lista.sort(reverse=True)
    print(f"Lista ordenada desc: {lista}")
    squared_list = square(lista)
    print(f"Cubo de los elementos : {squared_list}")

