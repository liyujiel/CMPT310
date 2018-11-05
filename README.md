# A* search in matrix
## Description
The assignment question is a variation of Find Shortest Path. The input is the start and goal location in a Matrix(Graph). I decided to choose A* algorithm for better performance than Dijkstra algorithm because A* Algorithm contains benefits from Dijkstra and Best-first Search Algorithm. The implementation needs definition for `f(n) = g(n) + h(n)`. `g(n)` is the value of the location, but the heuristic `h(n)` is indecisive. After searching online, the physical distance between two locations is the heuristic value.

There is one thing I was trying to implement in this assignment is get the shortest path
without make pre-process of input which is make it as a graph object. At this point, each time my
script searches the current location will try to get 4 different side locations as neighbor and check
it still in the range by check location coordinates.

After I got the goal location, another problem I faced is the assignment required return a
list of target. It will waste space and hard to keep if I use a list contains visited location through
searching process. So, I create a map named came_from, each time I get a better result, I will
store the neighbor location as key, and current location as value. Once the search is done, I can
track back the target location recursively or return “Not Found”.

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
