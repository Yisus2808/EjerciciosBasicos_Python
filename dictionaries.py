# product = {
#     "name": "book",
#     "quantity": 3,
#     "price": 16.90
# }

# person = {
#     "firts_name": "Yisus",
#     "last_name": "Perez",
#     "nickname": "KimiNox"
# }

# print(type(product))
# # print(dir(person))
# print(person.keys())
# print(person.items())

# from random import randint, uniform, random

# cantidad_tarjetas = 3
# parar = 1

# bin = ['5','2','2','4','4','5','x','x','x','x','x','x','x','x','x','x'] #BIN QUE RECIBO 
# bin_for = bin # BIN PARA EL FOR

# bin_copy = []
# tarjeta = [] # tarjeta que se guarda

# dict_bin = {
#     'BIN': bin,
#     'TARJETAS': tarjeta
#     }

# while parar <= cantidad_tarjetas:
    
#     print(f"Para: {parar} Pidio: ",cantidad_tarjetas)
    
#     for index, datos_bin in enumerate(bin_for):
#         if datos_bin == 'x' or datos_bin == 'X':
#             datos_bin = randint(0,9)
            
#             print(f"Index: {index} Dato que elimino a la x: ",datos_bin)
            
#             bin_for.insert(index, datos_bin)
#             bin_for.pop(index + 1) #"pop quita el ultimo elemento"
    
#     tarjeta.append(bin_for)
#     bin_copy.append(bin)
    
#     # bin_for.clear()
    
#     bin.append(bin_copy)
    
#     parar = parar + 1
    
# print(bin)
# print(bin_for)
# print(bin_copy)
# print(tarjeta)
# print(dict_bin)

# def sumaLista(listaNumeros):
#     if len(listaNumeros) == 1:
#         return listaNumeros[0]
#     else:
#         return listaNumeros[0] + sumaLista(listaNumeros[1:])
# lista = [1,2,3,4,5,6,7,8,9,1,1,2,3,4,5,6]
# suma = sumaLista(lista)
# print(suma)
