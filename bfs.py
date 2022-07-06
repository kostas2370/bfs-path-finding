#e = empodio
#o = discovered

import numpy as np

        #0   1   2   3   4   5   6   7   8   9
map_1=[
       ['-','-','-','-','-','-','-','-','-','-'], #0
       ['-','-','e','-','e','-','-','-','-','-'], #1
       ['-','-','-','e','-','-','-','-','-','-'], #2
       ['-','-','-','-','-','-','-','-','-','-'], #3
       ['-','-','-','-','e','-','-','-','x','-'], #4
       ['-','-','-','-','-','-','e','e','e','-'], #5
       ['-','-','-','-','-','-','-','-','e','-'], #6
       ['-','-','-','-','-','-','-','-','e','*']  #7
       ]
def get_start(mapx):
    for i in range(len(mapx)):
        for j in range (len(mapx[0])):
            if mapx[i][j]=='*':
                return i,j

def get_neighbours(mapx,c):
    neighbours={}
   
    if mapx[c[0]-1][c[1]] != "e" and mapx[c[0]-1][c[1]] != "o" and c[0]-1!=-1 :
        neighbours["up"]= (c[0]-1,c[1] )
    if c[1]+1<len(mapx[0]):
        if mapx[c[0]][c[1]+1] != "e" and mapx[c[0]][c[1]+1] != "o" :
            neighbours["right"]= (c[0],c[1]+1)
    if c[0]+1<len(mapx):
        if mapx[c[0]+1][c[1]] != "e" and mapx[c[0]+1][c[1]] != "o"  :
            neighbours["down"]= (c[0]+1,c[1] )
    if mapx[c[0]][c[1]-1] != "e" and mapx[c[0]][c[1]-1] != "o" and c[1]!=0 :
        neighbours["left"]= (c[0],c[1]-1)
    return neighbours

def bfs(st,mapx):
    queue=[]
    close=[]
    result=[]
    if (mapx[st[0]][st[1]]=='x'):
        return "first"
    for y in get_neighbours(mapx,st):
        queue.append(get_neighbours(mapx,st)[y])
    while len(queue)!=0:
        
        current=queue.pop(0)

        close.append(current)
        if mapx[current[0]][current[1]] =="x":
          
            print("Found !")
            return close
        z=get_neighbours(mapx,current)
        for p in z:
            if z[p] not in queue and z[p]  not in close:
                
                queue.append(get_neighbours(mapx,current)[p])
        print (f"{np.matrix(mapx)}\n \n")
        
        mapx[current[0]][current[1]]="o"

        
    print("queue :")
    return len(queue)

current=get_start(map_1)

print(bfs(current,map_1))
