import copy

initial_state = [[
    [4, 1, 2],
    [7, 5, 3],
    [0, 8, 6]
]]

goal_state = [[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]]


print("\t Initial state")
for i in range(0,1):
    for j in range(0,3):
        print(initial_state[i][j])


print("\t Goal state")
for i in range(0,1):
    for j in range(0,3):
        print(goal_state[i][j])

#Initialize the possible states/frontier
queue = []

#Initialize the visited states or P
first_visited_state = copy.deepcopy(initial_state)

#Breath-First Search
iteraciones = 0


while first_visited_state[iteraciones] != goal_state[0] and iteraciones <= 10000:

    #Help to find the row and column of zero
    zero_row_col = [0,0]
    aux = 0
    #for n in range(iteraciones):
    for i in range(0,3):
        for j in range(0,3):
            if first_visited_state[iteraciones][i][j] == 0:
                zero_row_col[0]=i
                zero_row_col[1]=j
                print("Zero here: " + str(zero_row_col))
    aux = aux + 1 

    #Expand the parent state of first_visited_state
    #Move up
    if(zero_row_col[0] > 0):
        change_val = copy.deepcopy(first_visited_state[iteraciones])
        change_val[zero_row_col[0]][zero_row_col[1]] = first_visited_state[iteraciones][zero_row_col[0]-1][zero_row_col[1]]
        change_val[zero_row_col[0]-1][zero_row_col[1]] = 0
        queue.append(change_val)
        #print(queue)

    #Move down
    if(zero_row_col[0] < 2):
        change_val = copy.deepcopy(first_visited_state[iteraciones])
        change_val[zero_row_col[0]][zero_row_col[1]] = first_visited_state[iteraciones][zero_row_col[0]+1][zero_row_col[1]]
        change_val[zero_row_col[0]+1][zero_row_col[1]] = 0
        queue.append(change_val)
        #print(queue)

    #Move right
    if(zero_row_col[1] < 2):
        change_val = copy.deepcopy(first_visited_state[iteraciones])
        change_val[zero_row_col[0]][zero_row_col[1]] = first_visited_state[iteraciones][zero_row_col[0]][zero_row_col[1]+1]
        change_val[zero_row_col[0]][zero_row_col[1]+1] = 0
        queue.append(change_val)
        #print(queue)

    #Move left
    if(zero_row_col[1] > 0):
        change_val = copy.deepcopy(first_visited_state[iteraciones])
        change_val[zero_row_col[0]][zero_row_col[1]] = first_visited_state[iteraciones][zero_row_col[0]][zero_row_col[1]-1]
        change_val[zero_row_col[0]][zero_row_col[1]-1] = 0
        queue.append(change_val)
        #print(queue)
    
    #visit a new child state in the queue
    #print(queue[0])
    first_visited_state.append(queue[0]) #BFS
    queue.pop(0) #remove the visited state
    print("\t Actual state")

    
    iteraciones = iteraciones + 1
    print(iteraciones)
    print(first_visited_state[iteraciones]) 

print("Se terminó")
print(first_visited_state[iteraciones])
print(goal_state[0])