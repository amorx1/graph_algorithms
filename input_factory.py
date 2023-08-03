from abc import ABC, abstractmethod
from enum import Enum
import math

class AlgorithmType(Enum):
	BELLMAN_FORD = 0
	DIJKSTRA = 1
	KRUSKAL = 2
	PRIMS = 3
	KAHNS = 4
	FLOYD_WARSHALL = 5

class InputType(Enum):
	DICTIONARY = dict
	ADJACENCY_MATRIX = list

class Input(ABC):
	@abstractmethod
	def generate() -> InputType:
		pass

class DijkstraInput(Input):
	def __init__(self, input_type):
		self.input_type = input_type
	def generate(self) -> InputType:
		match self.input_type:
			case InputType.DICTIONARY:
				return {
						0:[(4,1), (2,2)],
						1:[(3,2), (3,3), (2,4)],
						2:[(1,1), (4,3), (5,4)],
						3:[],
						4:[(1,3)],
					}
			case InputType.ADJACENCY_MATRIX:
				return [
					[0, 4, 2, 0, 0],
					[0, 0, 3, 2, 3],
					[0, 1, 0, 4, 5],
					[],
					[0, 0, 0, 1, 0]
				]
			case _:
				return None


class BellmanFordInput(Input):
	def __init__(self, input_type):
		self.input_type = input_type
	def generate(self) -> InputType:
		match self.input_type:
			case InputType.DICTIONARY:
				return {
					0:[(8, 5), (10, 1)],
					1:[(2, 3)],
					2:[(1, 1)],
					3:[(-2, 2)],
					4:[(-4, 1), (-1, 3)],
					5:[(1, 4)]
				}
			case InputType.ADJACENCY_MATRIX:
				return [
                	[0, 10, 0, 0, 0, 8],
                	[0, 0, 0, 2, 0, 0],
                	[0, 1, 0, 0, 0, 0],
                	[0, 0, -2, 0, 0, 0],
                	[0, -4, 0, -1, 0, 0],
                	[0, 0, 0, 0, 1, 0]
				]
			case _:
				return None


class KruskalInput(Input):
	def __init__(self, input_type):
		self.input_type = input_type
	def generate(self) -> InputType:
		match self.input_type:
			case InputType.DICTIONARY:
				return {
            		'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
            		'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
            		'C': [(3, 'A', 'C'), (5, 'D', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
            		'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
            		'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
            		'F': [(9, 'G', 'F'), (8, 'E', 'F'), (7, 'D', 'F')],
            		'G': [(9, 'F', 'G')],
        		}
			case InputType.ADJACENCY_MATRIX:
				return [
                	[0, 2, 3, 3, math.inf, math.inf, math.inf],
                	[2, 0, 4, math.inf, 3, math.inf, math.inf],
                	[3, 4, 0, 5, 1, math.inf, math.inf],
                	[3, math.inf, 5, 0, math.inf, 7, math.inf],
                	[math.inf, 3, 1, math.inf, 0, 8, math.inf],
                	[math.inf, math.inf, math.inf, 7, 8, 0, 9],
                	[math.inf, math.inf, math.inf, math.inf, math.inf, 9, 0]
            	]
			case _:
				return None

class AbstractInputFactory(ABC):
	@abstractmethod
	def get_input(for_algorithm: AlgorithmType) -> InputType:
		pass

class InputFactoryProducer:
	@staticmethod
	def get_factory(input_type: InputType) -> AbstractInputFactory:
		match input_type:
			case InputType.DICTIONARY:
				return DictionaryInputFactory()
			case InputType.ADJACENCY_MATRIX:
				return AdjacencyMatrixInputFactory()
			case _:
				return None

class DictionaryInputFactory(AbstractInputFactory):
	@staticmethod
	def get_input(for_algorithm: AlgorithmType) -> InputType.DICTIONARY:
		match for_algorithm:
			case AlgorithmType.DIJKSTRA:
				return DijkstraInput(InputType.DICTIONARY).generate()
			case AlgorithmType.BELLMAN_FORD:
				return BellmanFordInput(InputType.DICTIONARY).generate()
			case AlgorithmType.KRUSKAL:
				return KruskalInput(InputType.DICTIONARY).generate()
			case _:
				raise ValueError("Algorithm not supported")

class AdjacencyMatrixInputFactory(AbstractInputFactory):
	@staticmethod
	def get_input(for_algorithm: AlgorithmType) -> InputType.ADJACENCY_MATRIX:
		match for_algorithm:
			case AlgorithmType.DIJKSTRA:
				return DijkstraInput(InputType.ADJACENCY_MATRIX).generate()
			case AlgorithmType.BELLMAN_FORD:
				return BellmanFordInput(InputType.ADJACENCY_MATRIX).generate()
			case AlgorithmType.KRUSKAL:
				return KruskalInput(InputType.ADJACENCY_MATRIX).generate()
			case _:
				raise ValueError("Algorithm not supported")

#####