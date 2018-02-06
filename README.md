# A*

I leave this question as a specific type of Find Shortest Path.

It contains start, goal location in a Matrix(Graph), the most common solution is Dijkstra algorithm.

But base on all search algorithm we learned in class, I decide to choice A* algorithm should have best performance in this type of question

There is 3 method in my python script:

    1. path_find(size, start_loc, goal_loc, values)
        Main function represent A* algorithm, I leave the step by step explaination as comments in my script

    2. heuristic(a,b)
        Heuristic function for calculate heuristic number, I use Pythagorean theorem for calculate distance between nodes

    3. reconstruct_path(came_from,current_node)
        Return a list of locations which use recursively method get current_node from dictionary named came_from