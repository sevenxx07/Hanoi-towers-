import copy
 
import numpy as np
 
from blockworld import BlockWorld
 
from queue import PriorityQueue
 
import blockworld
 
class BlockWorldHeuristic(BlockWorld):
    def __init__(self, num_blocks=5, state=None):
        BlockWorld.__init__(self, num_blocks, state)
 
    def heuristic(self, goal):
        self_state = self.get_state()
        goal_state = goal.get_state()
 
        sum = 0
        num = 0;
        for stack in self_state:
            num = len(stack)
            #print(f" stack len {len(stack)}")
            for goal_stack in goal_state:
                for i in range(1, len(stack)+1):
                    if(stack[-i] == goal_stack[-i]):
                        num -= 1
                    else:
                        break
                    if (i >= len(goal_stack)):
                        break
            sum += num
 
        return sum
 
class AStar():
    def reconstruct_path(self, visited, start, goal):
        # print("reconstruct")
        action, prev_state, heuristic, cost = visited[goal]
        path = [action]
        while prev_state != start:
            action, prev_state, heuristic, cost = visited[prev_state]
            path.append(action)
        # print(list(reversed(path)))
        return list(reversed(path))
 
    def search(self, start, goal):
        # ToDo. Return a list of optimal actions that takes start to goal.
        opened = PriorityQueue()
        visited = dict()
        prev_action = None
        prev_state = None
        current = copy.deepcopy(start)
        heuristic = current.heuristic(goal)
 
        cost = 0
        visited[current] = (prev_action, prev_state, heuristic, cost)
        opened.put((heuristic, current, cost))
 
        while not opened.empty():
            heuristic, current, cost = opened.get()
 
            if current == goal:
                return self.reconstruct_path(visited, start, goal)
 
            for action, neighbor in current.get_neighbors():
                next_state = copy.deepcopy(current)
                next_state.apply(action)
                heuristic = next_state.heuristic(goal) + cost
 
                if visited.get(next_state) is not None:
                    v_action, v_state, v_heuristic, v_cost = visited[next_state]
                    if cost < v_cost:
                        visited[next_state] = (action, current, heuristic, cost)
                        opened.put((heuristic, next_state, cost+1))
                else:
                    visited[next_state] = (action, current, heuristic, cost)
                    opened.put((heuristic, next_state, cost+1))
 
if __name__ == '__main__':
    # Here you can test your algorithm. You can try different N values, e.g. 6, 7.
    N = 5
 
    start = BlockWorldHeuristic(N)
    goal = BlockWorldHeuristic(N)
 
    print("Searching for a path:")
    print(f"{start} -> {goal}")
    print()
 
    astar = AStar()
    path = astar.search(start, goal)
 
    if path is not None:
        print("Found a path:")
        print(path)
 
        print("\nHere's how it goes:")
 
        s = start.clone()
        print(s)
 
        for a in path:
            s.apply(a)
            print(s)
 
    else:
        print("No path exists.")
 
    print("Total expanded nodes:", BlockWorld.expanded)
