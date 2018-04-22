'''
Dijkstra is a weighted and directed single source shortest path Algorithm
We have various network of nodes, with it is associated with a cost
We want to find all the nodes that a given source can reach with minimum cost
'''
#input the matrix from txt file
import numpy as np

input = np.loadtxt("weighted_directed.txt", dtype='i', delimiter=',')
# print(input)

#Dijkstra's algorithm using adjacency matrices
def dijkstra(input, m,source):
        k = 0
        cost = [[0 for x in range(m)] for x in range(1)]
        offsets = []
        order = [0]*m
        offsets.append(k)
        current = 0
        for j in range(m):
            cost[0][j] = input[k][j]
        mini = 999
        for x in range(m - 1):
            mini = 999
            for j in range(m):
                if cost[0][j] <= mini and j not in offsets:
                    mini = cost[0][j]
                    current = j
            offsets.append(current)
            for j in range(m):
                if cost[0][j] > cost[0][current] + input[current][j]:
                    cost[0][j] = cost[0][current] + input[current][j]
                    order[j] = current
        print"The shortest path", offsets
        print "Cost to all vertices in order", cost
        print "Path to vertices",order

#Entry point for program execution
print("Dijkstras algorithm graph using matrix representation ")
source = 0
m = n = len(input[0])
dijkstra(input, m, source)

