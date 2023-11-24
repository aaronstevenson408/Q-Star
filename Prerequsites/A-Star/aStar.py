import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mazelib import Maze
from mazelib.generate.Prims import Prims
from mazelib.generate.AldousBroder import AldousBroder
from mazelib.solve.BacktrackingSolver import BacktrackingSolver
from matplotlib.colors import ListedColormap
import time
import sys
import numpy  as np
import timeit

class AStar:
    def __init__(self, maze):
        self.maze = maze

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.insert(0, current)
        return total_path

    def a_star(self, start, goal):
        def heuristic(node):
            # Assuming a simple Euclidean distance heuristic for illustration
            return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5

        def get_neighbors(node):
            # Assuming movement is allowed in four directions (up, down, left, right)
            neighbors = []
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dir in directions:
                neighbor = (node[0] + dir[0], node[1] + dir[1])
                if 0 <= neighbor[0] < len(self.maze) and 0 <= neighbor[1] < len(self.maze[0]) and self.maze[neighbor[0]][neighbor[1]] != 1:
                    neighbors.append(neighbor)
            return neighbors

        def distance(node1, node2):
            # Assuming a simple distance of 1 between adjacent nodes
            return 1

        open_set = {start}
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start)}

        while open_set:
            current = min(open_set, key=lambda node: f_score[node])

            if current == goal:
                return self.reconstruct_path(came_from, current)

            open_set.remove(current)
            for neighbor in get_neighbors(current):
                tentative_g_score = g_score[current] + distance(current, neighbor)

                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                    if neighbor not in open_set:
                        open_set.add(neighbor)

        return None  # Open set is empty, but the goal was never reached

def showPNG(grid, start=None, end=None, path=None):
    """Generate a simple image of the maze with start, end points, and a path."""
    cmap = plt.cm.binary
    norm = plt.Normalize(vmin=0, vmax=1)

    plt.figure(figsize=(10, 5))

    # Color the grid based on the maze
    plt.imshow(grid, cmap=cmap, interpolation='nearest', norm=norm)

    # Highlight the start point in green
    if start:
        plt.scatter(start[1], start[0], color='green', marker='o', s=100, label='Start')

    # Highlight the end point in red
    if end:
        plt.scatter(end[1], end[0], color='red', marker='x', s=100, label='End')

    # Show the path if provided
    if path:
        path = np.array(path)
        plt.plot(path[:, 1], path[:, 0], color='blue', linewidth=2, label='Path')

    plt.xticks([]), plt.yticks([])
    plt.legend()
    plt.show()

m = Maze()
m.generator = AldousBroder(1000,100)
m.solver = BacktrackingSolver()
m.generate()
# m.generate_monte_carlo(10,1,.75)
m.generate_entrances(False,False)
showPNG(m.grid,m.start,m.end)
print(m.start)
print(m.end)
print(m.grid)
# a = AStar(m.grid,m.start,m.end)
# a.find_path()
# print(a.get_path())
astar = AStar(m.grid)

# Call the A* algorithm
start_node = m.start
start_time = time.time()
path = astar.a_star(start_node, m.end)
print("--- %s seconds ---" % (time.time() - start_time))
showPNG(m.grid,m.start,m.end,path= path)
print("Path:", path)