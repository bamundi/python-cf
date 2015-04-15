def funcion_basica(num1,num2):
	return num1 + num2

guardar_datos = funcion_basica(3,4)	
print guardar_datos

#puede o no llevar un valor por defecto (en este caso v=2)
# cuando va *algomas se refiere a una tupla
def mi_funcion(cad,v=2,*algomas):
	print cad * v
	for x in algomas:
		print x * v

mi_funcion('Python',3,'hola','chao',True, 5, 312)

#cuando va **algo mas se refiere a una diccionario
def mi_funcion2(cadena,veces=2,**diccionario):
	print cadena * veces

	print diccionario['segundo']
	

mi_funcion2('Python',3, primero = 'hola', segundo = 3 * 3)