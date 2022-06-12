
def tsp(dist, ans):
    minDist = 0.0
    for i in range(len(dist)-1):
        ind = ans[-1]-1
        mini = 0
        for j in range(1,len(dist)):
            if (dist[ind][mini] != -1 and mini+1 not in ans):
                break
            mini = j
        for j in range(mini,len(dist)):
            if dist[ind][j] < dist[ind][mini] and dist[ind][j] != -1 and j+1 not in ans:
                mini = j
        minDist += dist[ind][mini]
        ans.append(mini+1)
    return(ans, minDist)

def pita(cordFrom, cordTo):
    dist = ((cordTo[0]-cordFrom[0])**2 + (cordTo[1]-cordFrom[1])**2) ** (1/2)
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
    minDist = -1
    for i in range(n):
        tmpAns, tmpDist = tsp(dist, [i+1])
        tmpAns.append(tmpAns[0])
        tmpDist += dist[tmpAns[0]-1][tmpAns[-2]-1]
        if (minDist == -1):
            minDist = tmpDist
            ans = tmpAns
        if (tmpDist < minDist):
            minDist = tmpDist
            ans = tmpAns

    print("Długość drogi do przebycia: " + str(minDist))
    print("Minimalna droga do przebycia: " + ' -> '.join(list(map(str, ans))))