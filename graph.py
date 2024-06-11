'''visted=[]
queue=[]
for key in graph:
    queue.append(key)
    l=graph[key]
    for i in l:
        queue.append(i)
    if queue[0] not in visted:     
      visted.append(key)
    print(queue[0])
    queue.pop(0)
print(queue,visted)'''

graph={'B':['A','C','D'],'A':['B','C'],'C':['A','B','E'],'D':['B','E'],'E':['C','D']}
def bfs(start,graph):
   visted=[start]
   q=[start]
   while len(q)!=0:
      ele=q.pop(0)
      for i in graph[ele]:
         if i not in visted:
            q.append(i)
            visted.append(i)
   return visted
print(bfs('B',graph))


def dfs(start,graph,visted):
    visted.append(start)
    for key in graph[start]:
        if key not in visted:
           dfs(key,graph,visted)
    return visted
print(dfs('B',graph,[]))

     
   


        

      
    
    
    