from abc import ABC, abstractmethod
import input_factory
from input_factory import InputType
import math
import heapq

class Solver(ABC):
	@abstractmethod
	def solve():
		pass

class DijkstraSolver(Solver):
	def __init__(self):
		self.graph = None
		self.input_type = None

	def set_graph(self, graph):
		self.graph = graph

	def set_input_type(self, input_type):
		self.input_type = input_type
		
	def solve(self, start: int) -> dict:
		match self.input_type:
			case InputType.DICTIONARY:
				shortest_paths = {}
				for node in self.graph:
					shortest_paths[node] = math.inf
				
				shortest_paths[start] = 0
				visited = set()

				visited.add(start)

				heap = []

				heapq.heappush(heap, (0, start))
	
				while heap:
					distance, node = heapq.heappop(heap)
					visited.add(node)

					for cost, to_node in self.graph[node]:
						if to_node not in visited and distance + cost < shortest_paths[to_node]:
							shortest_paths[to_node] = distance + cost
							heapq.heappush(heap, (shortest_paths[to_node], to_node))
					
				return shortest_paths
			case InputType.ADJACENCY_MATRIX:
				n = len(self.graph)
				shortest_paths = {i:math.inf for i in range(n)}
				shortest_paths[start] = 0
				visit = set()
				visit.add(start)

				heap = [(0, start)]
				while heap:
					distance, to_node = heapq.heappop(heap)
					visit.add(to_node)
					for nxt_node, cost in enumerate(self.graph[to_node]):
						if cost != 0 and nxt_node not in visit and distance + cost < shortest_paths[nxt_node]:
							shortest_paths[nxt_node] = distance + cost
							heapq.heappush(heap, (shortest_paths[nxt_node], nxt_node))

				return shortest_paths
			case _:
				raise ValueError("Invalid input type")
			
class BellmanFordSolver(Solver):
	def __init__(self):
		self.graph = None
		self.input_type = None

	def set_graph(self, graph):
		self.graph = graph

	def set_input_type(self, input_type):
		self.input_type = input_type
		
	def solve(self, start: int) -> dict:
		match self.input_type:
			case InputType.DICTIONARY:
				shortest_paths = {}
				for node in self.graph:
					shortest_paths[node]=math.inf
				shortest_paths[start] = 0

				size = len(self.graph)

				for i in range(size-1):
					for node in self.graph:
						for cost, to_node in self.graph[node]:
							if shortest_paths[node] + cost < shortest_paths[to_node]:
								shortest_paths[to_node] = shortest_paths[node] + cost

				for node in self.graph:
					for cost, to_node in self.graph[node]:
						if shortest_paths[node] + cost < shortest_paths[to_node]:
							return 'Invalid - cycle detected'

				return shortest_paths
			
			case InputType.ADJACENCY_MATRIX:
				n = len(self.graph)
				shortest_paths = [math.inf] * n
				shortest_paths[start] = 0

				for i in range(n-1):
					for node in range(n):
						for nxt, cost in enumerate(self.graph[node]):
							if cost != 0 and shortest_paths[node] + cost < shortest_paths[nxt]:
								shortest_paths[nxt] = shortest_paths[node] + cost

				for node in range(n):
					for nxt, cost in enumerate(self.graph[node]):
						if cost != 0 and shortest_paths[node] + cost < shortest_paths[nxt]:
							return 'Invalid graph - negative cycle'

				return shortest_paths
			case _:
				raise ValueError("Invalid input type")