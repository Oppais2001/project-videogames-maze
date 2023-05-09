import networkx as nx
import random
def crea_grafo_unidireccional(n,m):#Crea grafo con todas las rutas posibles
    grafo = nx.DiGraph()
    #Agregar nodos
    for i in range(n):
        for j in range(m):
            grafo.add_node((i+1, j+1))
    #Agrega aristas horizontales
    for i in range(n):
        for j in range(m-1):
            grafo.add_edge((i+1, j+1), (i+1, j+2))
    #Agregar aristas verticales
    for i in range(n-1):
        for j in range(m):
            grafo.add_edge((i+1, j+1), (i+2, j+1))
    #Crea las conexiones de vuelta
    #Agrega aristas horizontales
    for i in range(n):
        for j in range(m-1):
            grafo.add_edge((i+1, j+2), (i+1, j+1))    
    #Agregar aristas verticales
    for i in range(n-1):
        for j in range(m):
            grafo.add_edge((i+2, j+1), (i+1, j+1))
    return grafo

def inicio_ruta(n, m):
    x = random.randint(1,n)
    if x==1:
        y = random.randint(2,m)
    elif(1<x and x<n):
        l=[1,m]
        y = random.choice(l)
    elif x==n:
        y = random.randint(1,m-1)
    #print("nodo inicial:", end=" ")
    #print(x,y)
    return x,y
    
def final_ruta(inicio,n, m):
    x1,y1 = inicio
    x = random.randint(1,n)
    while x==x1:
        x = random.randint(1,n)
    y=y1
    while y==y1:
        if x==1:
            y = random.randint(2,m)
        elif(1<x and x<n):
            l=[1,m]
            y = random.choice(l)
        elif x==n:
            y = random.randint(1,m-1)
    #print("nodo final:", end=" ")
    #print(x,y)
    return x,y
def dfs(node,node_final,visitados,grafo):
    visitados.append(node)
    #print("nodo base:", end=" ")
    #print(node)
    for vecinos in grafo[node]:
        if vecinos not in visitados:
            #print("nodos vecinos:", end=" ")
            #print(vecinos)
            if vecinos!=node_final:
                dfs(vecinos,node_final, visitados, grafo)
            else:
                visitados.append(vecinos)
                #print("Final")
                break
            return visitados
def GrafoaMatriz(n,m,lista):
    #print("De grafo a matriz")
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(" ")
    for a in lista:
        x, y = a
        indice=lista.index(a)
        matriz[x-1][y-1]="{}".format(indice)
    return matriz,indice
 
n=14
m=14
grafo=crea_grafo_unidireccional(n,m)
inicio=inicio_ruta(n,m)
final=final_ruta(inicio,n,m)
lista=[]
lista=dfs(inicio,final,lista,grafo)
#print(lista)
matriz,i=GrafoaMatriz(n,m,lista)
#print(i)
while i<195:
    inicio=inicio_ruta(n,m)
    final=final_ruta(inicio,n,m)
    lista=[]
    lista=dfs(inicio,final,lista,grafo)
    matriz,i=GrafoaMatriz(n,m,lista)
    
for x in range(n):
    print(matriz[x])
    
