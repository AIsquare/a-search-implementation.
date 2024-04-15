from __future__ import annotations
from heapq import heappush, heappop
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
#priority queue
"""
A* search uses priority queue as the data structure
for its frontier. A priority queue keesp its elements internal
orders, such that the first element propped out is
always the highest-priority element.
In our case highest element would be the one
with lowest f(n)

"""
"""
Heap data structure is mainly used to represent a 
priority queue. 
In Python, it is available using the “heapq” module. 
The property of this data structure in Python is that each time the smallest heap element is popped(min-heap).
"""


T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


class PriorityQueue(Generic[T]):
	def __init__(self):
		self._container = []

	@property
	def empty(self):
		return not self._container #not is true for empty container

	def push(self, item) -> None:
		heappush(self._container,item) # in by priority

	def pop(self):
		return heappop(self._container) # out by priority

	def __repr__(self):
		return repr(self._container)

def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    # work backwards from end to front
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path

def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    # frontier is where we've yet to go
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    # explored is where we've been
    explored: Dict[T, float] = {initial: 0.0}

    # keep going while there is more to explore
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        # if we found the goal, we're done
        if goal_test(current_state):
            return current_node
        # check where we can go next and haven't explored
        for child in successors(current_state):
            new_cost: float = current_node.cost + 1  # 1 assumes a grid, need a cost function for more sophisticated apps

            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None  # went through everything and never found goal