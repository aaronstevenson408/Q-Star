How does A Star Work: 
[![A* (A Star) Search Algorithm - Computerphile](https://img.youtube.com/vi/ySN5Wnu88nE/0.jpg)](https://www.youtube.com/watch?v=ySN5Wnu88nE)

![Adding of Distance plus Path via Solved](adding_of_distance_plus_path_via_solved.PNG)

![Adding of Distance plus Path via](adding_of_distance_plus_path_via.PNG)

Chooses the shorest path by taking in the lenght and weight of the paths , an optimized version of  Dijkstra's Algorithm

Bard youtube synopsis of a-star video:
Here is a summary of the video:

The video reviews the A* (A Star) search algorithm, which is a graph search algorithm that finds the shortest path between two nodes in a graph. The algorithm works by using a heuristic function to estimate the distance to the goal node, and then using this information to prioritize which nodes to explore next. The video also discusses how the A* algorithm can be used to find the shortest path between two points on a map.

The video starts by reviewing the Dijkstra algorithm, which is a similar graph search algorithm that does not use a heuristic function. The video then explains how the A* algorithm works, and how it can be used to find the shortest path between two nodes in a graph. The video also discusses how the A* algorithm can be used to find the shortest path between two points on a map.

Finally, the video discusses some of the limitations of the A* algorithm, and how it can be improved. The video also discusses some of the applications of the A* algorithm, such as in robotics and pathfinding. 

**I. Introduction**

**A. Problem Statement**

1. The goal is to find the shortest path between two points.
2. This problem is common in computer science and has many applications.

**B. Graph Representation**

1. A graph is a data structure used to represent relationships between entities.
2. Nodes represent entities, and edges represent relationships between entities.
3. Each edge has a weight, which represents the cost of traversing the edge.

# C. Dijkstra's Algorithm

##[![Dijkstra's Algorithm - Computerphile](https://img.youtube.com/vi/GazC3A4OQTE/0.jpg)](https://www.youtube.com/watch?v=GazC3A4OQTE)

## I. Introduction

### A. What is Dijkstra's Algorithm?

Dijkstra's algorithm is a path-finding algorithm for finding the shortest path between two nodes in a graph with non-negative edge path costs. It produces a shortest path tree, which is a tree containing all the shortest paths from the source node to all other nodes in the graph.

### B. Where is Dijkstra's Algorithm Used?

Dijkstra's algorithm is widely used in routing and navigation applications, such as GPS navigation systems and network routing protocols. It is also used in other areas, such as scheduling and optimization problems.

## II. Algorithm Overview

### A. Maintaining a Priority Queue

Dijkstra's algorithm maintains a priority queue of unvisited nodes with estimated distances from the source node. The lowest priority node is removed from the queue and updated with the distances to its neighbors. This process is repeated until all nodes have been visited or the destination node has been reached.

### B. Repetition until Completion

The algorithm continues to process nodes until all nodes have been visited or the destination node has been reached. Once the destination node has been reached, the shortest path to that node has been found.

## III. Limitations

### A. Negative Edge Path Costs

Dijkstra's algorithm is not suitable for graphs with negative edge path costs. This is because the algorithm relies on the assumption that the distance between two nodes is always non-negative.

### B. Direction of Travel

Dijkstra's algorithm does not consider the direction of travel, which can lead to suboptimal routes in graphs with one-way edges.

## IV. Extensions

### A. A* Algorithm

The A* algorithm is a variant of Dijkstra's algorithm that uses a heuristic to estimate the distance to the destination node. This can make the algorithm more efficient in some cases, especially when the heuristic is accurate.

[![Satellite Navigation - Computerphile](https://img.youtube.com/vi/EUrU1y5is3Y/0.jpg)](https://www.youtube.com/watch?v=EUrU1y5is3Y)

**D. A* Algorithm**

1. A* is an extension of Dijkstra's algorithm that uses a heuristic to improve its performance.
    ?? What is the Hueristic and can that change
2. A heuristic is a function that estimates the distance to the goal node.
3. A* is guaranteed to find the shortest path between two points if the heuristic is admissible.

**E. Applications**

1. A* is often used in applications where it is important to find the shortest path quickly, such as in route planning.
2. It is also used in other applications, such as robotics and pathfinding.



