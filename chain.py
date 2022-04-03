def getInNeighbors(G, node):
    lst = []
    for key, value in G.items():
        for i in value:
            if i == node:
                lst.append(key)
    return lst

def graph_gen(n, fun, points):
    G = dict()
    for i in range(n):
        G[i] = [(fun[i], points[i])]
    
    Gr = dict()
    for i in G.keys():
        Gr[i] = getInNeighbors(G, i)
    return Gr

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        # print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def maximum_fun(n, fun, points):
    G = graph_gen(n, fun, points)

    fun_score = 0; funcp = fun[:]; ppc = points[:]

    while 1:
        all_paths = []
        for i in range(n-1, -1, -1):
            if G[i][0]==None:
                continue

            path = []
            cost = 0
            
            j=i
            while(j>=0):
                cost += dict1[j][0]
                j=points[j]

            all_paths.append(sum(path))

    print(max(all_paths))

'''If I take all paths and then take their max'''


def main():
    visited = set()
    n_test = int(input())
    for i in range(n_test):
        n = int(input())
        fun = input.split()
        points = input.split()

        print("Case #"+str(i+1)+": ", end='')
        maximum_fun(n, fun, points)

main()