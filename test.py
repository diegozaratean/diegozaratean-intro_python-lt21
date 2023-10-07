## Javascript === Python
##    //.     === #
# console.log('hola') === print('hola')
# print('hola')
# generoPelicula === genero_pelicula
# integer, string , booleanos === integer, string , booleanos
# true === True
# null undefine === none
# array === Listas, Tuplas
# Objetos === Diccionarios

# last_name = 'zarate'
# edad = 38
# name = 'diego'
# esta_vivo = True
# print(name + last_name)
# print("hola mi nombre es" + name + last_name)
# # cast.   int(). 
# # int('5') => 5
# # str(1) => "1"
# print("mi edad es " + str(edad) )
# segundo_numero = '3'
# print(edad + int(segundo_numero))

# Declaración de Diccionarios
# js const objeto = {}
# persona = {
#     'nombre': 'diegp',
#     'apelido': 'zarate',
#     'edad': 38
# }
# print(persona)
# print(persona['nombre'])
# print(persona['edad'])

# # Declaración de Listas / Arrays
# # Js let array = [elemento1,elemento2]
# skills = ['js','react','css']
# print(skills)
# print(len(skills))
# skills.append('python')
# print(skills)
# print(len(skills))
# print(len('ad'))
# # skills.length() ==== len(skills)

# # Declaración de Tupla
# cardinals = ('Norte','Sur','Este','Oeste')
# print(cardinals)
# cardinals.append('Noreste')
# print(cardinals)


# Map y Lambda
# people_list = [{'name':'Diego'},{'name':'Santiago'},{'name':'Johana'}]
# # map(funcion lamnda que trabaja con el item,lista/array)
# # Js arrar.map( (item)=>  codigo que trabaja con item).  map(, array)
# # Js. (item)=>  codigo que trabaja con item). === lambda item: codigo que trabaja con item
# resultado = map(lambda person: person['name'] ,people_list)

# print(people_list)
# print(resultado)
# print(list(resultado))

# frutas = ['manzana','pera','mango']
# print(frutas)

# resultado = map(lambda fruta: fruta + 's',frutas)
# print(resultado)
# print(list(resultado))


# Funciones
# JS f
# function saludar(){
# console.log('donde estoy')
#}
#
# def saludar():
# print('Antes de la función')
# def saludar():
#     print(1)
# print(2)
# print(3)
# print('Despues  de la función')

# print(4)
# print(5)

# # saludar()
# # saludar()

# print('antes de saludar')
# def saludar(nombre):
#     print('hola ' + nombre)

# print('despues de saludar')

# saludar('diego')

# Procesos iterativos / Loops
# colores = ['amarillo','blanco','verde']

# for color in colores:
#     print(color)

# If / Else
# edad = 85
# if edad < 18:
#     print('No puedes tomar cerveza')
# elif edad < 80:
#     print('Puedes tomar cerveza')
# else:
#     print('Puedes tomar cerveza, pero no deberias')

# Class 
# class Carro:
#     def __init__(self,marca,color,cilindraje):
#         self.marca = marca
#         self.color = color
#         self.cilindraje = cilindraje

#     def serialize(self):
#         return {
#             "marca": self.marca,
#             "color": self.color,
#             "calificación": 'EL mejor carro',
#             "numero_de_llantas": 4
#             # "nombre": self.marca + str(self.cilindraje),
#             # "cilindraje": self.cilindraje
#         }


# huracan = Carro('lamborgini','gris con azul',4000)
# print(huracan.marca)
# print(huracan.color)
# print(huracan.cilindraje)

# print(huracan)
# print(huracan.serialize())


# class Desesperado:
#     def __init__(self,nombre,hobbies,cualidades,defectos,historial_relaciones):
#         self.nombre = nombre
#         self.hobbies = hobbies
#         self.cualidades = cualidades
#         self.defectos = defectos
#         self.historial_relaciones = historial_relaciones

#     def serialize(self):
#         return {
#             "hobbies": self.hobbies,
#             "cualidades": self.cualidades,
#             "estado_civil": 'Soltero',
#             "defectos": self.defectos,
#             "historial_relaciones": self.historial_relaciones,
#             # "nombre": self.marca + str(self.cilindraje),
#             # "cilindraje": self.cilindraje
#         }

# armando = Desesperado('Armando',['Correr' , 'programar' , 'Taekondo'],'Guapo, caballeroso, intelingente,nnnnnn','Canson, Ronca, Celoso, Tronco, Cantaletoso, Agresivo','2 divorcios, 15 realciones fallidos , 2 realciones que terminaron en bienestar familiar')
# gustavo = Desesperado('a',"b","c","d","e")
# print(armando)
# print(armando.serialize())

# print(gustavo.serialize())


# Paquetes
# JS npm  ====> package.json
# Python pip ===> pipfile
# Python pipenv ===> pipfile