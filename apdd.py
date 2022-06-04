

def apdEstadoFinal(Transiciones,Inicial,Final,palabra):
    s = []
    s.append('R')
    estado=[Inicial,palabra,s[0]]
    for i in palabra:
        print(i)
        for j in Transiciones:
            if estado[0]==j[0][0] and i==j[0][1]:
                estado[0]=j[1][0]
                estado[1]=estado[1][1:]
                print(estado)
                if(j[1][1]=='E'):
                    s=eliminarDelStack(s)
                else:
                    s=agregarAlStack(s,j[1][1])
                estado[2]=s[-1]
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
        for i in range(len(R)-2): #Si el largo de la palabra es mayor a 1, se agregan letras al stack, menos la ultima
            s.append(R[i])
            return s

def eliminarDelStack(s):
    s.pop()
    return s


transi=[]
sigue=True
print("Ingrese las transiciones de la forma (q0,a,R)=(q1,A), donde q es el estados,a la palabra y R es el elemento del stack")
while(sigue):
    tran=input("Ingrese la transicion:")
    abs=(tran.split('='))
    abs[0]=abs[0].strip()
    abs[0]=abs[0][1:len(abs[0])-1].split(',')
    abs[1]=abs[1].strip()
    abs[1]=abs[1][1:len(abs[1])-1].split(',')
    transi.append(abs)
    xd=input("quiere ingresar otra transicion (N:no,Y:si):")
    if(xd=="N" or xd=="n"):
        sigue=False

estadoInicial=input("ingrese estado inicial:")
estadoFinal=False
xd=input("De que forma el APD acepta las palabras?, ingrese '1' si es por estado final o '2' si es por stack vacio:")
if(xd=="1"):
    estadoFinal=True
    final=input("ingrese estado final:")
palabraEntrada=input("Ingrese palabra de entrada:")

if(estadoFinal==True):
    print("entre")
    apdEstadoFinal(transi,estadoInicial,final,palabraEntrada)
