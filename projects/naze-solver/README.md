# 

# Maze Solver using Dijkstra's Algorithm

This project implements a maze solver using **Dijkstra's algorithm**, optimized object creation, and a graphical user interface (GUI) built with **Tkinter** and **Pygame**. The solver finds the shortest path between two points in a maze image, which can be selected by the user through the GUI.

## Features

- **Dijkstra's Algorithm**: Utilizes the Dijkstra algorithm to find the shortest path between two points in the maze.
- **Optimized Object Creation**: Efficiently manages node creation and heap operations for improved performance.
- **Graphical User Interface**: Allows users to load maze images, select start and end points, and visualize the shortest path found by the solver.
- **Real-time Interaction**: Users can interact with the maze and dynamically visualize the pathfinding process.

## Running the Solver

To run the solver, ensure you have the required dependencies installed and use the following command:

```bash
python main.py
```

## Directory Structure

```
project_root/
│
├── README.md               # Project documentation
├── src/                    # Source code for the simulation
│   ├── main.py             # Entry point for the game
│   ├── maze_solver.py      # Core logic of the maze solver using Dijkstra's algorithm
│   ├── gui.py              # GUI logic for interacting with the maze solver
├── public/                 # Contains all graphical and sound assets
│   ├── example_maze.png    # Example maze image for testing
```

## How It Works

1. **Load an Image**: The user loads a maze image using the "Load Image" button.
2. **Select Points**: Click on the maze image to set the start and end points.
3. **Run Solver**: Click the "Run" button to start the solver, which will display the shortest path found.
4. **Refresh**: Click the "Refresh" button to reset the maze and select new points.

![Maze solution](https://github.com/yakkovwaxelbom/work-basket/blob/main/projects/naze-solver/public/Maze%20solution.png)


## Future Improvements

- **Advanced Pathfinding Algorithms**: Explore other pathfinding algorithms like A* and BFS for comparison.
- **More Features in GUI**: Implement additional user controls for zooming, panning, and customizing the maze.
- **Support for Dynamic Mazes**: Allow users to modify the maze structure in real-time and see updated paths.

## Technologies Used

- **Python**
- **Tkinter**: For the graphical user interface.
- **Pygame**: For handling image processing and visualization.
- **OpenCV**: For image processing and manipulation.
