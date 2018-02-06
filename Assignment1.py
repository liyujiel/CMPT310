'''

CMPT310 Assignment 1
Author: Alex Li

'''

from queue import PriorityQueue
import ast

# read the grid size
size = int(input("Grid size: "))

# read the start/goal location
start_loc = ast.literal_eval(input("Start location: "))

goal_loc = ast.literal_eval(input("Goal location: "))

# the array of values
values = ast.literal_eval(input("Array of values: "))
# print(type(values))


# Use Pythagorean theorem as heuristic function
def heuristic(a,b):
    (x1,y1) = a
    (x2,y2) = b
    return abs(x1-x2) + abs(y1-y2)


# return path and recursively get the came_from node
def reconstruct_path(came_from,current_node):
    if current_node!=None:
        if came_from.get(current_node):
            p = reconstruct_path(came_from, came_from[current_node])
            return p+[current_node]
        else:
            return [current_node]

# use A* search algorithm
def path_find(size, start_loc, goal_loc, values):
    # initalize variables, g_score(goal score), h_score(heuristic score), 
    # f_score is a PriorityQueue contains location and  h_score[location] as priority
    g_score = {}
    h_score = {}
    f_score = PriorityQueue()

    # closedSet, openSet are two sets for track visited and willing visite locations, 
    # openset should contains start point as first start location
    closedset = set()
    openset = set()
    openset.add(start_loc)

    # came_from contains the location come from.
    # initially, start location should came from None
    came_from = {}
    came_from[start_loc] = None

    # initalize g_score, h_score, f_score values
    g_score[start_loc] = 0
    h_score[start_loc] = heuristic(start_loc,goal_loc)
    f_score.put(start_loc,h_score[start_loc])
    while len(openset)!=0:
        curr = f_score.get()
        if(curr == goal_loc):
            return reconstruct_path(came_from,goal_loc)
        if(curr in openset):
            openset.remove(curr)
        closedset.add(curr)
        for neighbour in ((curr[0]-1,curr[1]),(curr[0]+1,curr[1]),(curr[0],curr[1]-1),(curr[0],curr[1]+1)):
            if(0<neighbour[0]<=size and 0< neighbour[1]<=size):
                if(neighbour in closedset):
                    continue
                tentative_g_score = g_score[curr] + int(values[neighbour[0]-1][neighbour[1]-1])

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
    return "Not Found"        


# Call path_find method and print result
least_cost_path = path_find(size, start_loc, goal_loc, values)
print(least_cost_path)
