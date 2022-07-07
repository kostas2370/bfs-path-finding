#e = empodio
#o = discovered

import numpy as np
import pprint
        #0   1   2   3   4   5   6   7   8   9
map_1=[
       ['-','-','-','-','-','-','-','-','-','-'], #0
       ['-','-','e','e','e','e','e','e','e','e'], #1
       ['-','-','-','e','-','-','-','-','-','-'], #2
       ['-','-','e','-','-','e','e','-','e','e'], #3
       ['-','-','e','-','e','x','e','-','-','-'], #4
       ['-','-','-','-','-','-','e','e','e','-'], #5
       ['-','-','e','-','-','-','-','-','e','-'], #6
       ['-','-','-','-','-','-','-','-','e','*']  #7
       ]
def get_start(mapx):
    for i in range(len(mapx)):
        for j in range (len(mapx[0])):
            if mapx[i][j]=='*':
                return i,j
def find_path(maps, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return path
        if start not in maps:
            return None
        
        for node in maps[start]:
            if node not in path:
               
                newpath = find_path(maps, node, end, path)
                if newpath: return newpath
        return None

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
    lista=[]
    x={}
    for j in get_neighbours(mapx,st): lista.append(get_neighbours(mapx,st)[j])
        
    x[st]=set(lista)
    mapx[st[0]][st[1]]='o'
    if (mapx[st[0]][st[1]]=='x'):
        return "first"
    for y in get_neighbours(mapx,st):queue.append(get_neighbours(mapx,st)[y])
    while len(queue)!=0:
        lista =[]  
        current=queue.pop(0)
        z=get_neighbours(mapx,current)
        if mapx[current[0]][current[1]] =="x":
            for p in get_neighbours(mapx,current):lista.append(get_neighbours(mapx,current)[p])
            x[current]=set(lista)
            j=find_path(x,st,current)
            return j

        for p in z:
            if z[p] not in queue and z[p]  not in x:
                queue.append(get_neighbours(mapx,current)[p])
                lista.append(get_neighbours(mapx,current)[p])
        print(f"{np.matrix(mapx)} \n \n")

        x[current]=set(lista)
        mapx[current[0]][current[1]]="o"
        
    return "not in list"

current=get_start(map_1)

print(bfs(current,map_1))



    