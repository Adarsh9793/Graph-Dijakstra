from queue import PriorityQueue

adjMatrix = [[0,3,5,0] , [0,0,1,4] , [0,0,0,0] , [0,0,0,2]]

def shortedPath(adjMatrix , a , b):
    ans = dict()
    nodes = PriorityQueue() 
    src = a
    nodes.put((0,src))
    vis = dict()

    while nodes.empty() == False:
        (currDist , currNode) = nodes.get()
        print(currNode , currDist)

        vis[currNode] = 1
        if ans.get(currNode) == None:
            ans[currNode] = currDist

        for i in range(len(adjMatrix)):
            if adjMatrix[currNode-1][i] > 0 and vis.get(i+1) != 1:
                nodes.put((currDist + adjMatrix[currNode-1][i] , i+1))

    return ans.get(b)
print(shortedPath(adjMatrix , 1 , 4))

