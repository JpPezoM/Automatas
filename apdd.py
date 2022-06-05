

def apdEstadoFinal(Transiciones,Inicial,Final,palabra):
    s = []
    s.append('R')
    estado=[Inicial,palabra,s]
    for i in palabra:
        for j in Transiciones:
            if estado[0]==j[0][0] and i==j[0][1] and estado[2][-1]==j[0][2]:
                estado[0]=j[1][0]
                estado[1]=estado[1][1:]
                if(j[1][1]!='E'):
                    s=agregarAlStack(s,j[1][1])
                else:
                    s=eliminarDelStack(s)
                break
            else:
                print("No se acepta la palabra") 
                return
    print(s)
    if(estado[0]==Final):
        print("La palabra es aceptada")
        return
    print("No se acepta la palabra")    
    
def agregarAlStack(s,R):
    if (len(R) == 1):
        print(1) 
        return s #No agrega nada porque se mantiene intacto el stack
    else:
        for i in range(len(R)-1): #Si el largo de la palabra es mayor a 1, se agregan letras al stack, menos la ultima
            s.append(R[i])
            return s

def eliminarDelStack(s):
    s.pop()
    return s


transi=[]
sigue=True
print("Ingrese las transiciones de la forma (q0,a,R)=(q1,A), donde 'q0' y 'q1' son los estados,'a' la palabra y 'R' y 'A' elementos del stack,coinsidere que 'E' es la palabra vacia")
while(sigue):
    tran=input("Ingrese la transicion:")
    if(tran==""):
        sigue=False
    else:
        abs=(tran.split('='))
        abs[0]=abs[0].strip()
        abs[0]=abs[0][1:len(abs[0])-1].split(',')
        abs[1]=abs[1].strip()
        abs[1]=abs[1][1:len(abs[1])-1].split(',')
        transi.append(abs)
    #xd=input("quiere ingresar otra transicion (N:no,Y:si):")
    #if(xd=="N" or xd=="n"):
        #sigue=False
    

estadoInicial=input("ingrese estado inicial:")
estadoFinal=True
#xd=input("De que forma el APD acepta las palabras?, ingrese '1' si es por estado final o '2' si es por stack vacio:")
#if(xd=="1"):
    #estadoFinal=True
final=input("ingrese estado final:")
palabraEntrada=input("Ingrese palabra de entrada:")

if(estadoFinal==True):
    apdEstadoFinal(transi,estadoInicial,final,palabraEntrada)
