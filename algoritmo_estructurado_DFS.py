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
    pared=str("")
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
            
    if y==1:
        pared="izquierda"
    elif y==m:
        pared="derecha"
    if x==1:
        pared="arriba"
    elif x==n:
        pared="abajo"
        
    #print("nodo final:", end=" ")
    #print(x,y)
    return (x,y),pared
def dfs(node,node_final,visitados,grafo,):
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
def GrafoaMatriz(n,m,lista,pared):#De grafo a matriz
    matriz = []
    for i in range((2*n)+1):
        matriz.append([])
        for j in range((2*m)+1):
            matriz[i].append("X")
    for a in range(len(lista)):
        x, y = lista[a]
        indice=a
        matriz[(2*x)-1][(2*y)-1]="{}".format(" ")
        if a+1<len(lista):
            x1,y1 = lista[a+1]
            if x==x1:
                if y-y1==1:#"i"
                    matriz[(2*x)-1][(2*y)-2]=" "
                elif y-y1==-1:#"d"
                    matriz[(2*x)-1][(2*y)]=" "
            if y==y1:
                if x-x1==1:#"s"
                    matriz[(2*x)-2][(2*y)-1]=" "
                elif x-x1==-1:#"b"
                    matriz[(2*x)][(2*y)-1]=" "
        if a==0:
            matriz[(2*x)-1][(2*y)-1]="p"
        if a+1==len(lista):
            if pared=="arriba":
                matriz[(2*x)-2][(2*y)-1]=" "
            if pared=="abajo":
                matriz[(2*x)][(2*y)-1]=" "
            if pared=="izquierda":
                matriz[(2*x)-1][(2*y)-2]=" "
            if pared=="derecha":
                matriz[(2*x)-1][(2*y)]=" "
    return matriz,indice

def imprime_matriz(matriz):   
    for lista in matriz:
        print("[", end=" ")
        for elemento in lista:
            print(elemento, end=" ")
        print("]")

n=14
m=14
grafo=crea_grafo_unidireccional(n,m)
inicio=inicio_ruta(n,m)
final,pared=final_ruta(inicio,n,m)
lista=[]
lista=dfs(inicio,final,lista,grafo)
matriz,i=GrafoaMatriz(n,m,lista,pared)
while i<195:
    inicio=inicio_ruta(n,m)
    final,pared=final_ruta(inicio,n,m)
    lista=[]
    lista=dfs(inicio,final,lista,grafo)
    matriz,i=GrafoaMatriz(n,m,lista,pared)
#print(lista)
#print(final, pared)
imprime_matriz(matriz)
#print(grafo)