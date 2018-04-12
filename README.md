# Maze problem
Standing at the entrance of the maze and looking for an exit. We have to find a path to the exit and count how many nodes were visited before reaching the exit.   

There can be various ways to solve this problem; I am trying to solve it by using following ways:
1)	unweighted_BFS_via_vertex_matrix: In this program we are reading adjacent matrices from “unweighted_undirected_vertex_matrix.csv”   
  1 if there is a path,       
  0 if no path exists.   
Then we do Breadth First Search(BFS), BFS by default is unweighted and not directed. <br />

2) Dijkstra_algorithm: In this program we are reading adjacent matrices from "weighted_directed.txt"
Dijkstra is a weighted and directed single source shortest path Algorithm
  We have a various network of nodes, with it is associated with a cost
  We want to find all the nodes that a given source can reach with minimum cost
  
-----------------------------------
The unweighted_undirected_vertex_matrix is as follows 

1    —    6  —  20&nbsp;  —&nbsp;  8 — 4 — 12 — 11    
|&emsp;&emsp;|&emsp;&emsp;|&emsp;&emsp;&emsp;|&emsp;&emsp;   
21&nbsp;&nbsp;&nbsp;18 &emsp;10&emsp;&emsp;9 — 5   
/ \ &emsp;|	&emsp;&emsp;&emsp;&emsp;&emsp;|    
2  3 &nbsp;&nbsp;7—15—14&nbsp;&nbsp;&nbsp;19    
&emsp;&emsp;/\ &emsp;|         
&emsp;16&nbsp;17&nbsp;13    

