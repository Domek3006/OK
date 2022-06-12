import time
import random

def conSol(phero, dist, i, ans):
    global alp, beta
    #alp = 0.21                 #współczynnik ważności feromonów
    #beta = 10              #współczynnik ważności odległości
    s = 0.0
    p = -1
    for j in range(len(dist)):
        if (dist[i][j] == -1):
            continue
        s += (phero[i][j]**alp)*(dist[i][j]**(-1*beta))
    '''if s == 0:
        minDist = -1
        for j in range(len(dist)):
            if ((dist[i][j] < minDist) or (minDist == -1)) and (dist[i][j] != -1) and (j+1 not in ans):
                minDist = dist[i][j]
                ind = j
        return(ind)'''
    for j in range(len(dist)):
        ptmp = ((phero[i][j]**alp)*((dist[i][j]**-1)**(beta)))/s
        if ((ptmp > p) or (p == -1)) and (j+1 not in ans):
            p = ptmp
            ind = j
    return(ind)

def localpher(edge,i,j):
    global ro, tau
    #ro = 0.4                #szybkość wyparowywania
    #tau = 1.0               #parametr początkowy feromonów
    pher = ((1-ro)*edge[i][j]) + (ro*tau)
    edge[i][j] = pher
    edge[j][i] = pher
    return

def globalpher(edge, minDist):
    global ro
    #ro = 0.4
    for i in range(len(edge)):
        for j in range(len(edge)):
            if edge[i][j] == 0:
                continue
            edge[i][j] = ((1-ro)*edge[i][j]) + (ro*(minDist**-1))
    return

def pita(cordFrom, cordTo):
    dist = ((cordTo[0]-cordFrom[0])**2 + (cordTo[1]-cordFrom[1])**2) ** (1/2)
    if(dist == 0.0):
        print("NOOOOO",cordFrom,cordTo)
    return(dist)

def distCount(cords, dist):
    for i in range(len(cords)):
        for j in range(len(cords)):
            if (i == j):
                dist[i].append(-1)
            else:
                dist[i].append(pita(cords[i], cords[j]))
    return

while (input("Stop? [y/n] ").strip() != "y"):
    cords = list()    
    dist = list()
    edge = list()
    fi = open(input("Podaj nazwę pliku: ").strip(), "r")
    n = int(fi.readline())
    for i in range(n):
        tmp = fi.readline()
        tmp = list(map(float, tmp.split()))
        cords.append([tmp[1],tmp[2]])
        tmp = None
        dist.append([])
    fi.close()
    distCount(cords, dist)
    '''minDist = -1
    cords = None
    ans = None'''
    '''for i in range(len(dist)):
        edge.append([tau]*len(dist))'''
    #step = len(dist) % 3
    #start = -1*step

    #n = 15              #liczba iteracji
    #m = 20              #liczba mrówek
    alp = float(input("Parametr alfa: ").strip())
    beta = float(input("Parametr beta: ").strip())
    ro = float(input("Parametr ro: ").strip())
    tau = float(input("Parametr tau: ").strip())
    m = int(input("Liczba mrówek: ").strip())
    T = float(input("Czas pracy w sekundach: ").strip())
    Ttmp = T

    timeStart = time.time()
    minDist = -1
    ans = None
    edge = list()
    for i in range(len(dist)):
        edge.append([tau]*len(dist))
    #for i in range(n):
    while True:
        while (time.time()-timeStart < T):
            startList = list()
            for j in range(m):
                """start += step
                if (start >= len(dist)):
                    start -= len(dist)
                    start += 1"""
                start = random.randint(0, len(dist)-1)
                while (start in startList):
                    start = random.randint(0, len(dist)-1)
                anstmp = list()
                anstmp.append(start+1)
                distTmp = 0
                while(len(anstmp)!=len(dist)):
                    nxt = conSol(edge, dist, anstmp[-1]-1, anstmp)
                    anstmp.append(nxt+1)
                    localpher(edge, anstmp[-2]-1, nxt)
                    distTmp += dist[anstmp[-2]-1][nxt]
                if (distTmp < minDist) or (minDist == -1):
                    minDist = distTmp
                    ans = anstmp
            globalpher(edge, minDist)
        ans.append(ans[0])
        minDist += dist[ans[-2]-1][ans[-1]-1]
        print("Długość drogi do przebycia: " + str(minDist))
        T += Ttmp
    print("Minimalna droga do przebycia: " + ' -> '.join(list(map(str, ans))))