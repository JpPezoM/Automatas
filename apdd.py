
def apdEstadoFinal(Transiciones,Inicial,Final,palabra):
    s = []
    s.append('R')
    estado=[Inicial,palabra,s[0]]
    for i in palabra:
        for j in Transiciones:
            if estado[0]==j[0][0] and i==j[0][1] and estado[2]==j[0][2]:
                estado[0]=j[1][0]
                
def agregarAlStack(s,R):
    if len(R)==1:
        if R==s[-1]:
            return s
        else:
            s.pop()
            return s
    else:
        ActualStack=s[-1]
        for i in R:
            if i==ActualStack:
                
            s.append(i)






    

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

inicial=input("ingrese estado inicial:")
estadofinal=False
xd=input("De que forma el APD acepta las palabras?, ingrese '1' si es por estado final o '2' si es por stack vacio:")
if(xd=="1"):
    estadofinal=True
    final=input("ingrese estado final:")

palabraEntrada=input("Ingrese palabra de entrada:")

print(transi[0][0][0])