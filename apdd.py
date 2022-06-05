import sys

def agregarAlStack(s,R):
    if (len(R) == 1): 
        return s #No agrega nada porque se mantiene intacto el stack
    else:
        for i in range(len(R)-1): #Si el largo de la palabra es mayor a 1, se agregan letras al stack, menos la ultima
            s.append(R[i])
        return s

def eliminarDelStack(s):
    s.pop()
    return s

def apdEstadoFinal(Transiciones,Inicial,Final,palabra):
    s = ['R']
    estado = [Inicial, palabra, s]
    QuedaPalabra = True
    while(QuedaPalabra):
        if(estado[1]==""):
            estado[1]="E"
            QuedaPalabra=False
        for j in Transiciones:
            if estado[0]==j[0][0] and estado[1][0]==j[0][1] and estado[2][-1]==j[0][2]:
                estado[0]=j[1][0]
                estado[1]=estado[1][1:]
                if(j[1][1]!='E'):
                    s=agregarAlStack(s,j[1][1])
                else:
                    s=eliminarDelStack(s)
                break
            elif(j==Transiciones[len(Transiciones)-1]):
                print("La palabra no es aceptada")
                return
    if(estado[0]==Final):
        print("La palabra es aceptada")
        return
    print("No se acepta la palabra")    
    
def apdStackVacio(Transiciones,Inicial,palabra):
    s = ['R']
    estado = [Inicial, palabra, s]
    QuedaPalabra = True
    while(QuedaPalabra):
        if(estado[1]==""):
            estado[1]="E"
            QuedaPalabra=False
        for j in Transiciones:
            if estado[0]==j[0][0] and estado[1][0]==j[0][1] and estado[2][-1]==j[0][2]:
                estado[0]=j[1][0]
                estado[1]=estado[1][1:]
                if(j[1][1]!='E'):
                    s=agregarAlStack(s,j[1][1])
                else:
                    s=eliminarDelStack(s)
                break
            elif(j==Transiciones[len(Transiciones)-1]):
                print("La palabra no es aceptada")
                return
    if(len(s)==0):
        print("La palabra es aceptada")
        return
    print("No se acepta la palabra")        

def procesaEntrada(entrada):
    abs=(entrada.split('='))
    abs[0]=abs[0].strip()
    abs[0]=abs[0][1:len(abs[0])-1].split(',')
    abs[1]=abs[1].strip()
    abs[1]=abs[1][1:len(abs[1])-1].split(',')
    return abs

transi=[]
forma=input("En que forma quiere que se lean sus transiciones(1:Leer desde txt; 2:Ingresar manualmente):")
print("RECUERDE:ingresar las transiciones de la forma (q0,a,R)=(q1,A), donde 'q0' y'q1' son los estados,'a'",
     " la palabra y 'R' y 'A' elementos del stack,coinsidere que 'E' es la palabra vacia")

if (forma == "2"):
    print("Para dejar de ingresar transiciones se debe ingresar ''")
    tran = input("Ingrese la transicion:")
    while(tran):
        transi.append(procesaEntrada(tran))
        tran=input("Ingrese la transicion:")
elif(forma=="1"):
    with open("./transi.txt","r") as archivo:
        for tran in archivo:
            transi.append(procesaEntrada(tran))
else:
    sys.exit("Debe igresar una opcion")

estadoInicial=input("ingrese estado inicial:") #Quizá se deberia verificar que el estado inicial existe

metodo=input("De que forma el APD acepta las palabras?, ingrese '1' si es por estado final o '2' si es por stack vacio:")
while (metodo != '1' and metodo != '2'):
    print("Error. Ingrese una opción valida")
    metodo=input("De que forma el APD acepta las palabras?, ingrese '1' si es por estado final o '2' si es por stack vacio:")

if (metodo == "1"):
    final=input("ingrese estado final:")

cont = '2'
while (cont == '2'):
    palabraEntrada=input("Ingrese palabra de entrada:")
    if (metodo == "1"): apdEstadoFinal(transi,estadoInicial,final,palabraEntrada) 
    else: apdStackVacio(transi,estadoInicial,palabraEntrada)
    cont = input("Desea ingresar otra palabra (1:no, 2:si):") #En realidad se detiene para cualquier cosa que no sea 2 :T

print("Programa Finalizado")