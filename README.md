# Maze problem
Standing at the entrance of the maze and looking for an exit. We have to find a path to the exit and count how many nodes were visited before reaching the exit.   

The maze is as follows 

1    —    6  —  20&nbsp;  —&nbsp;  8 — 4 — 12 — 11    
|&emsp;&emsp;|&emsp;&emsp;|&emsp;&emsp;&emsp;|&emsp;&emsp;   
21&nbsp;&nbsp;&nbsp;18 &emsp;10&emsp;&emsp;9 — 5   
/ \ &emsp;|	&emsp;&emsp;&emsp;&emsp;&emsp;|    
2  3 &nbsp;&nbsp;7—15—14&nbsp;&nbsp;&nbsp;19    
&emsp;&emsp;/\ &emsp;|         
&emsp;16&nbsp;17&nbsp;13    

There can be various ways to solve this problem; I am trying to solve it by using following ways:
1)	BFS_using_vertices_matrix: “vertices_matrix.csv” provides the path.  1 if there is a path, 0 if no path exists. Then we do Breadth First Search(BFS) using this adjacency matrix.
