import networkx as nx
import random
def inicio_ruta(n, m, grafo):
    x = random.randint(1,n)
    if x==1:
        y = random.randint(1,m)
        print("x es 1")
        print("y puede estar entre 1 y m")
    elif(1<x or x<n):
        print("x esta entre 1 y n")
        l=[1,m]
        y = random.choice(l)
        print(y)
        print("y deberia ser 1 o n")
    elif x==n:
        print("x es igual a n")
        y = random.randint(1,m)
        print("y puede estar entre 1 y m")
    print("nodo de inicio:", end=" ")
    print(x,y)
    conexiones=[]
    contador = 0
    for edge in (grafo.edges):
        if x==y:
            x1,y1 = edge[0]
            if x==x1 and y==y1:
                x2,y2 = edge[1]
                if es_esquina(x1,y1,x2,y2,n,m,contador):
                    conexiones.append((x2,y2))
                    contador = 1
        else:
            x1, y1 = edge[0] #valores del nodo inicial
            if x1==x and y1==y:
                #print(edge[0]) # nodo de inicio
                x2, y2 = edge[1] #nodo conectado
                if es_borde(x2,y2,n,m):
                    conexiones.append((x2 , y2))
    print("Posibles conexiones:", end=" ")
    print(conexiones)
    Grafo_Ruta=nx.DiGraph()
    ruta1=random.choice(conexiones)
    for i in range(n):
        for j in range(m):
            Grafo_Ruta.add_node((i+1,j+1))
    Grafo_Ruta.add_edge((x,y),(ruta1))
    #Grafo_Ruta.add_edge((ruta1),(x,y))
    Lista_de_conexiones = []
    Lista_de_conexiones.append((x,y))
    Lista_de_conexiones.append(ruta1)
    return Lista_de_conexiones,ruta1,Grafo_Ruta

def sgte_ruta(lista,n,m,ruta1,grafo1,grafo2):
    conexiones=[]
    print(ruta1)
    for edge in grafo2.edges:
        if ruta1==edge[0]:
            x,y=edge[1]
            if es_borde(x,y,n,m):
                conexiones.append((x,y))
    print(conexiones)
    nueva_ruta=random.choice(conexiones)
    for node in grafo1.nodes:
        if ruta1==node:
            grafo1.add_edge((ruta1),(nueva_ruta))
            #grafo1.add_edge((nueva_ruta), (ruta1))
    lista.append(nueva_ruta)
    return lista, nueva_ruta, grafo1
        
def es_esquina(x, y, x1, y1 ,n, m, contador):#Retorna True si es esquina
    if es_borde(x1, y1, n, m):
        if(contador == 0):
            n1=x-x1
            n2=y-y1
            if(n1==-1):
                if(n2==1):
                    return True
                elif(n2==-1):
                    return True
            elif(n1==1):
                if(n2==1):
                    return True
                elif(n2==-1):
                    return True
        return False
    return False
def es_borde(x, y, n, m):#Retorna False si es borde
    if x==1:
        return False
    elif x==n:
        return False
    else:
        if y==1:
            return False
        elif y==m:
            return False
        else:
            return True

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
    #Agregar aristas diagonales
    for i in range(n-1):
        for j in range(m-1):
            grafo.add_edge((i+1, j+1), (i+2, j+2))
    for i in range(n-1):
        for j in range(m):
            if j!=0:
                grafo.add_edge((i+1, j+1), (i+2, j))
    #Crea las conexiones de vuelta
    #Agrega aristas horizontales
    for i in range(n):
        for j in range(m-1):
            grafo.add_edge((i+1, j+2), (i+1, j+1))    
    #Agregar aristas verticales
    for i in range(n-1):
        for j in range(m):
            grafo.add_edge((i+2, j+1), (i+1, j+1))
    #Agregar aristas diagonales
    for i in range(n-1):
        for j in range(m-1):
            grafo.add_edge((i+2, j+2), (i+1, j+1))
    for i in range(n-1):
        for j in range(m):
            if j!=0:
                grafo.add_edge((i+2, j), (i+1, j+1))
    return grafo

def imprime_grafo(grafo):
    for edge in grafo.edges:
        print(edge)
        
            
#PROGRAMA PRINCIPAL
n = int(input("Ingrese la cantidad de nodos verticales del grafos:"))
m = int(input("Ingrese la cantidad de nodos horizontales del grafo:"))
laberinto = crea_grafo_unidireccional(n,m)
Lista, ruta1,Camino = inicio_ruta(n, m, laberinto)
for i in range(5):
    Lista, ruta1,Camino=sgte_ruta(Lista,n,m,ruta1,Camino,laberinto)
print(Lista)

#final = valida_ruta(x, y, m, n)
