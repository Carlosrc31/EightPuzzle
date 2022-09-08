from time import time
from queue import PriorityQueue

class State:
    AStar_evaluation = None
    heuristic = None

    def __init__(self, state, parent, direction, depth, cost):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth
        self.goal = list(range(1, nSize*nSize)) + [0]

        if parent:
            self.cost = parent.cost + cost

        else:
            self.cost = cost

    def test(self): 
        if self.state == self.goal:
            return True
        return False

    def Manhattan_Distance(self, n):
        self.heuristic = 0
        for i in range(1, n*n):
            distance = abs(self.state.index(i) - self.goal.index(i))

            self.heuristic = self.heuristic + distance/n + distance % n

        self.AStar_evaluation = self.heuristic + self.cost

        return self.AStar_evaluation

    @staticmethod
    def available_moves(x, n):
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n-1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n*n - 1:
            moves.remove('Down')

        return moves

    def expand(self, n):
        x = self.state.index(0)
        moves = self.available_moves(x, n)

        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]

            children.append(State(temp, self, direction, self.depth + 1, 1))
        return children

    def solution(self):
        solution = []
        solution.append(self.direction)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.direction)
        solution = solution[:-1]
        solution.reverse()
        return solution


def AStar_search(given_state, n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    evaluation = root.Manhattan_Distance(n)
    frontier.put((evaluation, counter, root))  

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n)
                frontier.put((evaluation, counter, child))
    return


global nSize
nSize = int(input("Enter n\n"))
print("Enter your", nSize, "*", nSize, "puzzle")
root = []
for i in range(0, nSize*nSize):
    p = int(input())
    root.append(p)

print("The given state is:", root)


def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1, len(puzzle)):
            if ((puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv


def solvable(puzzle):
    inv_counter = inv_num(puzzle)
    if (inv_counter % 2 == 0):
        return True
    return False


if solvable(root):
    print("There is solution, please wait. \n")

    time4 = time()
    AStar_solution = AStar_search(root, nSize)
    AStar_time = time() - time4
    print('A* Solution is ', AStar_solution[0])
    print('Number of explored nodes is ', AStar_solution[1])
    print('A* Time:', AStar_time)


else:
    print("There is not solution")
