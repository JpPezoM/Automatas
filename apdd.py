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
print("RECUERDE:ingresar las transiciones de la forma (q0,a,R)=(q1,A), donde 'q0' y'q1' son los estados,'a'",
     " la palabra y 'R' y 'A' elementos del stack,coinsidere que 'E' es la palabra vacia\n")

forma=input("En que forma quiere que se lean sus transiciones \n 1:Leer desde txt (Primero debe editar el archivo 'transiciones.txt' ubicado en la carpeta del programa) \n 2:Ingresar manualmente \n Ingrese opcion:")

print()

if (forma == "2"):
    print("Para dejar de ingresar transiciones se debe ingresar ''")
    tran = input("Ingrese la transicion:")
    while(tran):
        transi.append(procesaEntrada(tran))
        tran=input("Ingrese la transicion:")
elif(forma=="1"):
    with open("./transiciones.txt","r") as archivo:
        for tran in archivo:
            transi.append(procesaEntrada(tran))
else:
    sys.exit("Debe igresar una opcion")

estadoInicial=input("ingrese estado inicial:") 
while (estadoInicial == "" or estadoInicial[0] != 'q'): #Valida que se ingrese un estado inicial de la forma correspondiente
    estadoInicial=input("Por favor ingrese un estado inicial valido (ej: 'q0'):")

metodo=input("De que forma el APD acepta las palabras?, ingrese '1' si es por estado final o '2' si es por stack vacio:")
while (metodo != '1' and metodo != '2'):
    print("Error. Ingrese una opción valida")
    metodo=input("De que forma el APD acepta las palabras?, ingrese '1' si es por estado final o '2' si es por stack vacio:")

if (metodo == "1"):
    final=input("ingrese estado final:")
    while (final == "" or final[0] != 'q'): #Valida que se ingrese un estado final de la forma correspondiente
        final=input("Por favor ingrese un estado final valido (ej: qf):")

cont = '2'
while (cont == '2'):
    palabraEntrada=input("Ingrese palabra de entrada:")
    if (metodo == "1"): apdEstadoFinal(transi,estadoInicial,final,palabraEntrada) 
    else: apdStackVacio(transi,estadoInicial,palabraEntrada)
    cont = input("Desea ingresar otra palabra (1:no, 2:si):") #En realidad se detiene para cualquier cosa que no sea 2 :T

print("Programa Finalizado")