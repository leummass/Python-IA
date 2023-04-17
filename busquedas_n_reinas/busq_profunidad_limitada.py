import time
from tableroreinas import ChessboardGUI


visitados = []
def CalcularAtaques(lista):
    length = len(lista)
    Ataques = 0
    for i in range(length-1):
        for j in range(i+1,length):
            if(lista[i]==lista[j]):
                Ataques+=2
            elif((abs(i-j)-abs(lista[i]-lista[j]))==0):
                Ataques+=2
    return Ataques

def GoalTest(lista):
    Numero_Ataques = CalcularAtaques(lista)
    if(Numero_Ataques==0):
        return True
    else:
        return False

def P_F(F,limite):
    if len(F)<0:
        print("No hay solucion")
        return
    edo_act = F[0][0]
    nvl_act = F[0][1]
    visitados.append(edo_act)
    print("Edo_act ",edo_act," Nivel ",nvl_act)
    F.pop(0)
    if GoalTest(edo_act):
        print("Solución: ",edo_act, "Nivel: ", nvl_act)
        gui = ChessboardGUI(4, visitados)
        return
    elif nvl_act < limite: 
        OS = expandir(edo_act,nvl_act)
        F = OS + F
    P_F(F,limite)

def expandir(edo_act,nvl_act):
    V = []
    n = len(edo_act)
    nvl_act = nvl_act+1
    for i in range(n):
        listAux = edo_act.copy()
        if (listAux[i]<n-1):
            listAux[i]=listAux[i]+1
            valorAux = [listAux,nvl_act]
            if listAux not in visitados:
                V.append(valorAux)
    return V
start_time = time.time()
P_F([[[0, 0, 0,0],0]],6)
print("--- %s seconds ---" % (time.time() - start_time))

