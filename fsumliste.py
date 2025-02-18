def sommaliste(lista1,lista2):   
 lista3=lista1+lista2
 return lista3

def sommalista(lista):
 somma=sum(lista)
 return somma

listaprima=[1,2,3,4,5]
listaseconda=[5,6,7,8]
listaterza=sommaliste(listaprima,listaseconda)
sommalista1=sommalista(listaprima)
print(listaterza)
print(sommalista1)