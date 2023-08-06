from abc import ABC, abstractmethod
from ctypes import Union
import input_factory
from input_factory import InputType
import utils
from utils import UnionFind
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
		if not self.input_type:
			raise ValueError("An input type must be set first")
		if not self.graph:
			raise ValueError("No graph exists")
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
				shortest_paths = {}
				for node in range(n):
					shortest_paths[node] = math.inf
				shortest_paths[start] = 0

				visit = set()
				visit.add(start)

				heap = []
				heapq.heappush(heap, (0, start))
				
				while heap:
					distance, node = heapq.heappop(heap)
					visit.add(node)
					for to_node, cost in enumerate(self.graph[node]):
						if cost != 0 and to_node not in visit and distance + cost < shortest_paths[to_node]:
							shortest_paths[to_node] = distance + cost
							heapq.heappush(heap, (shortest_paths[to_node], to_node))

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
		if not self.input_type:
			raise ValueError("An input type must be set first")
		if not self.graph:
			raise ValueError("No graph exists")
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
							raise ValueError('Invalid input - negative cycle detected')

				return shortest_paths
			
			case InputType.ADJACENCY_MATRIX:
				n = len(self.graph)
				shortest_paths = {i:math.inf for i in range(n)}
				shortest_paths[start] = 0

				for i in range(n-1):
					for node in range(n):
						for nxt, cost in enumerate(self.graph[node]):
							if cost != 0 and shortest_paths[node] + cost < shortest_paths[nxt]:
								shortest_paths[nxt] = shortest_paths[node] + cost

				for node in range(n):
					for nxt, cost in enumerate(self.graph[node]):
						if cost != 0 and shortest_paths[node] + cost < shortest_paths[nxt]:
							raise ValueError('Invalid input - negative cycle detected')

				return shortest_paths
			case _:
				raise ValueError("Invalid input type")
			
class KruskalSolver(Solver):
	def __init__(self):
		self.graph = None
		self.input_type = None

	def set_graph(self, graph):
		self.graph = graph

	def set_input_type(self, input_type):
		self.input_type = input_type
		
	def solve(self, start: int) -> list:
		assert self.input_type is not None
		assert self.graph is not None
		match self.input_type:
			case InputType.DICTIONARY:
				total_cost = 0
				MST = []
				n_nodes = 0
				edges = []

				for _, item in self.graph.items():
					n_nodes += 1
					edges.extend(item)

				edges.sort()

				uf = UnionFind(n_nodes)

				for cost, node1, node2 in edges:
					if uf.find(node1) != uf.find(node2):
						total_cost += cost
						uf.union(node1, node2)
						MST.append((cost, node1, node2)) 

				print(f"Minimum cost: {total_cost}")
				return MST
			
			case InputType.ADJACENCY_MATRIX:
				res = 0
				MST = []
				n = len(self.graph)
				uf = UnionFind(n)

				edges = [(self.graph[i][j], i, j) for j in range(n) for i in range(n) if self.graph[i][j] != 0 and self.graph[i][j] != math.inf]

				edges.sort()

				for cost, n1, n2 in edges:
					if uf.find(n1) != uf.find(n2):
						res += cost
						uf.union(n1,n2)
						MST.append((cost, n1, n2))

				print(f"Minimum cost: {res}")
				return MST
			
			case _:
				raise ValueError("Invalid input type")
			
class PrimsSolver(Solver):
	def __init__(self):
		self.graph = None
		self.input_type = None

	def set_graph(self, graph):
		self.graph = graph

	def set_input_type(self, input_type):
		self.input_type = input_type
		
	def solve(self, start: int) -> list:
		assert self.input_type is not None
		assert self.graph is not None
		match self.input_type:
			case InputType.DICTIONARY:
				seen, unseen = set(), set(list(self.graph.keys()))
				heap = self.graph[start]
				heapq.heapify(heap)
				seen.add(start)
				unseen.remove(start)
				MST, total_cost = [], 0

				while unseen:
					cost, from_node, to_node = heapq.heappop(heap)
					new_node = None

					if from_node in seen and to_node in unseen:
						new_node = to_node
						MST.append((cost, from_node, to_node))
					elif to_node in seen and from_node in unseen:
						new_node = from_node
						MST.append((cost, from_node, to_node))

					if new_node:
						seen.add(new_node)
						unseen.remove(new_node)
						total_cost += cost
						for nxt in self.graph[new_node]:
							heapq.heappush(heap, nxt)

				print(total_cost)
				return MST
			
			case InputType.ADJACENCY_MATRIX:
				seen, unseen = set(), set(list(range(len(self.graph))))
				heap = [(cost, to, start) for to, cost in enumerate(self.graph[start])]
				heapq.heapify(heap)
				seen.add(start)
				unseen.remove(start)
				MST, total_cost = [], 0

				while unseen:
					cost, from_node, to_node = heapq.heappop(heap)
					new_node = None
					if from_node in seen and to_node in unseen:
						new_node = to_node
						MST.append((cost, from_node, to_node))
					elif to_node in seen and from_node in unseen:
						new_node = from_node
						MST.append((cost, from_node, to_node))

					if new_node:
						seen.add(new_node)
						unseen.remove(new_node)
						total_cost += cost

						for nxt, cost in enumerate(self.graph[new_node]):
							if cost != 0 and cost != math.inf:
								heapq.heappush(heap, (cost, nxt, new_node))
				
				print(total_cost)
				return MST
			
			case _:
				raise ValueError("Invalid input type")