# A* search in matrix
## Description
The assignment question is a variation of Find Shortest Path. The input is the start and goal location in a Matrix(Graph). A* algorithm outperforms Dijkstra algorithm because A* Algorithm contains benefits from Dijkstra and Best-first Search Algorithm. The implementation needs definition for `f(n) = g(n) + h(n)`. `g(n)` is the value of the location, but the heuristic `h(n)` is indecisive. After searching online, the physical distance between two locations is the heuristic value.

## Achievement
Use a graph object to avoid pre-processing inputs for the shortest path. The script will check for in-range condition in 4 neighbor location coordinates for each "current location". 

The assignment requires to return a list of target. A list containing visited location is space-inefficient and unmanageable. So, the script will use a map named `came_from` to store the best neighbor location as key and current location as value in each update. The script will track back the target location recursively or return “Not Found” after search completes.

## Overview of the script
There are 3 methods in my python script:
1. path_find(size, start_loc, goal_loc, values)
Main function represents A* algorithm, I leave the step by step explanation as comments in
my script.
2. heuristic(a,b)
Heuristic function for calculate heuristic number, I use Pythagorean theorem for calculate
distance between nodes.
3. reconstruct_path(came_from,current_node)
Return a list of locations which use recursively method get current_node from dictionary
named came_from.
