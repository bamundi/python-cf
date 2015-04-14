lista = [True,4,6,2,"hola",32,3]

lista[5] = "chao" #reemplazar el 5to elemento desde el 0

listados = lista[0:2] #imprime los elementos en unrango entre 0 y 1
listatres = lista[0::3] #imprime los elementos de dos en dos en este caso True, 2 y 3

listacuatro = lista[0:5:2] #imprime los elementos en unrango entre 0 y 4 (por el 5) saltando de 1 en 1 (por el 2)

lista[0:2] = [9,0] #reemplaza elementos, en este caso entre 0 y 1 (por el 2)

lista[2:4] = [233] #reemplaza dos elementos por uno, en este caso entre 2 y 3 (por el 4)

listacinco = lista[-1] #en negativo comienza a recorrer la lista en orden inverso

print len(lista) #saber cuantos elementos tiene
print type(lista) #saber de que tipo es 'list' en este caso
print lista
print listados
print listatres
print listacuatro
print listacinco
