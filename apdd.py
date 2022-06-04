
transi=[]

sigue=True
print("Ingrese las transiciones de la forma (q,a,R)=(1,A), donde q es el estados,a la palabra y R es el elemento del stack")
"""while(sigue):
    
    xd=input("quiere ingresar otra transicion (N:no,Y:si):")
    if(xd=="N"):
        sigue=False"""
tran=input("Ingrese la transicion:")
abs=(tran.split('='))
abs[0]=abs[0].strip()
abs[0]=abs[0][1:len(abs[0])-1].split(',')
abs[1]=abs[1].strip()
abs[1]=abs[1][1:len(abs[1])-1].split(',')
transi.append(abs)
print(transi)
print(type(abs[0]))