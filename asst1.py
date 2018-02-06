'''

CMPT310 Assignment 1
Author: Alex Li

'''

from queue import PriorityQueue
import ast

# Read the grid size
size = 5 #int(input("Grid size: "))

# Read the start/goal location
start_loc = (1,1) #ast.literal_eval(input("Start location: "))

goal_loc = (5,4) #ast.literal_eval(input("Goal location: "))

# The array of values
values =  [[4,3,3,4,2],[2,4,4,2,2],[3,4,5,3,2],[2,3,4,5,2],[4,3,3,2,4]]#ast.literal_eval(input("Array of values: "))


# Use Pythagorean theorem as heuristic function
def heuristic(a,b):
    (x1,y1) = a
    (x2,y2) = b
    return abs(x1-x2) + abs(y1-y2)


# Return path and recursively get the came_from node
def reconstruct_path(came_from,current_node):
    if current_node!=None:
        if came_from.get(current_node):
            p = reconstruct_path(came_from, came_from[current_node])
            return p+[current_node]
        else:
            return [current_node]

# Use A* search algorithm
def path_find(size, start_loc, goal_loc, values):
    # Initalize variables, g_score(the cost from current location to target location), h_score(heuristic cost), 
    # f_score is a PriorityQueue contains location and  h_score[location] as priority
    g_score = {}
    h_score = {}
    f_score = PriorityQueue()

    # ClosedSet, openSet are two sets for track visited and willing visite locations, 
    # openset should contains start point as first start location
    closedset = set()
    openset = set()
    openset.add(start_loc)

    # came_from contains the location come from.
    # And set start location came from None
    came_from = {}
    came_from[start_loc] = None

    # Initalize g_score, h_score, f_score values
    g_score[start_loc] = 0
    h_score[start_loc] = heuristic(start_loc,goal_loc)
    f_score.put(start_loc,h_score[start_loc])

    # Start search from current the lowest cost node
    while len(openset)!=0:
        curr = f_score.get()

        # If current location is the target location, use reconstruct_path function to return a list of node path
        if(curr == goal_loc):
            return reconstruct_path(came_from,goal_loc)

        # Remove current node from non-visited set, we will start searching from this node, and add it in to visited set
        if(curr in openset):
            openset.remove(curr)
        closedset.add(curr)
        
        # Check all neighbours(4 sides) and make sure each neighbour location is still in the valid range
        for neighbour in ((curr[0]-1,curr[1]),(curr[0]+1,curr[1]),(curr[0],curr[1]-1),(curr[0],curr[1]+1)):
            if(0<neighbour[0]<=size and 0< neighbour[1]<=size):
                # If neighbour already visited, jump over to next neighbour
                if(neighbour in closedset):
                    continue

                # Calculate the tentative cost use the value from start to current plus neighbour
                tentative_g_score = g_score[curr] + int(values[neighbour[0]-1][neighbour[1]-1])

                # If we not check current neighbour point yet, or current g_score smaller than the old neighbour's g_score
                # we should set the flag we found a better path, and keep searching
                # Otherwise, this path is end
                if(not neighbour in openset):
                    openset.add(neighbour)
                    tentative_is_better = True
                elif tentative_g_score < g_score[neighbour]:
                    tentative_is_better = True
                else:
                    tentative_is_better = False
                
                if tentative_is_better == True:
                    came_from[neighbour] = curr
                    g_score[neighbour] = tentative_g_score
                    h_score[neighbour] = heuristic(neighbour,goal_loc)
                    f_score.put(neighbour,h_score[neighbour])
    # Once we searched all start_loc related point and still not found the goal_loc, return "Not Found"
    return "Not Found"        


# Call path_find method and print result
least_cost_path = path_find(size, start_loc, goal_loc, values)
print(least_cost_path)
