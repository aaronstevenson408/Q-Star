import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mazelib import Maze
from mazelib.generate.Prims import Prims
from mazelib.generate.AldousBroder import AldousBroder
from mazelib.solve.BacktrackingSolver import BacktrackingSolver
from matplotlib.colors import ListedColormap
import numpy  as np
import screeninfo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AStar:
    def __init__(self, maze, start, end, animation_speed=200):
        self.maze = maze
        self.start = start
        self.end = end
        self.steps = []
        self.shortest_path = []
        self.animation_speed = animation_speed

    def reconstruct_path(self, came_from, current):
        """Reconstruct the path from start to current using came_from dictionary."""
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.insert(0, current)
        return total_path

    def a_star(self):
        """Implement the A* algorithm to find the shortest path from start to goal."""
        start, goal = self.start, self.end

        def heuristic(node):
            """Heuristic function for estimating the cost from node to goal."""
            return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5

        def get_neighbors(node):
            """Get neighboring nodes that are valid and not obstacles."""
            neighbors = []
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for delta_x, delta_y in directions:
                neighbor = (node[0] + delta_x, node[1] + delta_y)
                if 0 <= neighbor[0] < len(self.maze) and 0 <= neighbor[1] < len(self.maze[0]) and self.maze[neighbor[0]][neighbor[1]] != 1:
                    neighbors.append(neighbor)
            return neighbors

        def distance(node1, node2):
            """Distance function for the cost of moving from node1 to node2."""
            return 1

        open_set = {start}
        came_from = {}
        cost_so_far = {start: 0}
        estimated_total_cost = {start: heuristic(start)}

        while open_set:
            current = min(open_set, key=lambda node: estimated_total_cost[node])

            if current == goal:
                path = self.reconstruct_path(came_from, current)
                self.steps.append(path)

                if not self.shortest_path or len(path) < len(self.shortest_path):
                    self.shortest_path = path

                return path

            open_set.remove(current)
            for neighbor in get_neighbors(current):
                tentative_g_score = cost_so_far[current] + distance(current, neighbor)

                if tentative_g_score < cost_so_far.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    cost_so_far[neighbor] = tentative_g_score
                    estimated_total_cost[neighbor] = tentative_g_score + heuristic(neighbor)
                    if neighbor not in open_set:
                        open_set.add(neighbor)

                # Record the current state for animation
                current_state = {
                    "open_set": list(open_set),
                    "came_from": came_from.copy(),
                    "cost_so_far": cost_so_far.copy(),
                    "estimated_total_cost": estimated_total_cost.copy(),
                }
                self.steps.append(current_state)

        return None  # Open set is empty, but the goal was never reached

    def print_steps(self):
        for i, step in enumerate(self.steps):
            print(f"Step {i + 1}:")
            if isinstance(step, list):  # A* path
                print("  A* Path:", step)
            else:  # Animation state
                print("  Animation State:")
                print("    Open Set:", step['open_set'])
                print("    Came From:", step['came_from'])
                print("    Cost So Far:", step['cost_so_far'])
                print("    Estimated Total Cost:", step['estimated_total_cost'])
            print()

    def generate_animation(self):
        """Generate an animation to visualize the A* algorithm."""
        fig, ax = plt.subplots()
        maze_array = np.array(self.maze)

        def update(frame):
            ax.cla()  # Clear axis
            ax.imshow(maze_array, cmap='gray_r')

            if frame < len(self.steps):
                step = self.steps[frame]

                if isinstance(step, list):  # A* path
                    path_array = np.array(step)
                    ax.plot(path_array[:, 1], path_array[:, 0], color='blue', marker='o')
                else:  # Animation state
                    # Visualize start and end nodes
                    ax.scatter(self.start[1], self.start[0], color='green', marker='o', s=100, label='Start')
                    ax.scatter(self.end[1], self.end[0], color='red', marker='x', s=100, label='End')

                    # Visualize open set
                    for node in step['open_set']:
                        ax.text(node[1], node[0], 'O', ha='center', va='center', color='green', fontsize=8)

                    # Visualize came_from
                    for node, came_from_node in step['came_from'].items():
                        ax.arrow(came_from_node[1], came_from_node[0], node[1] - came_from_node[1], node[0] - came_from_node[0],
                                shape='full', lw=0, length_includes_head=True, head_width=0.3, color='orange')

                    ax.set_title(f"Frame {frame + 1}/{len(self.steps)}")

            # Add other plot elements if needed


        # Rest of the code remains the same
        ani = animation.FuncAnimation(fig, update, frames=len(self.steps), repeat=False, interval=self.animation_speed)
        plt.show()
    def showPNG(self):
        """Generate a simple image of the maze with start, end points, and a path."""
        cmap = plt.cm.binary
        norm = plt.Normalize(vmin=0, vmax=1)

        plt.figure()

        # Color the grid based on the maze
        plt.imshow(self.maze, cmap=cmap, interpolation='nearest', norm=norm)

        # Highlight the start point in green
        if self.start:
            plt.scatter(self.start[1], self.start[0], color='green', marker='o', s=100, label='Start')

        # Highlight the end point in red
        if self.end:
            plt.scatter(self.end[1], self.end[0], color='red', marker='x', s=100, label='End')

        # Show the path if provided
        if self.shortest_path:
            path_array = np.array(self.shortest_path)
            plt.plot(path_array[:, 1], path_array[:, 0], color='blue', linewidth=2, label='Path')

        plt.xticks([]), plt.yticks([])
        plt.legend()

        # Center the window on the screen
        screen = plt.get_current_fig_manager().window
        screen_width, screen_height = screen.winfo_screenwidth(), screen.winfo_screenheight()
        window_width, window_height = plt.gcf().get_size_inches()
        screen.geometry(f"{int((screen_width - window_width) / 2)}x{int((screen_height - window_height) / 2)}+0+0")

        plt.show()


m = Maze()
m.generator = AldousBroder(1000,100)
m.solver = BacktrackingSolver()
m.generate()
# m.generate_monte_carlo(10,1,.75)
m.generate_entrances(False,False)

astar = AStar(m.grid,m.start,m.end,5)
astar.shortest_path = astar.a_star()

print("Shortest Path:", astar.shortest_path)
# astar.generate_animation()
astar.showPNG()