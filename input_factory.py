from abc import ABC, abstractmethod
from enum import Enum, auto
import math
from typing import Literal, Optional, Type

class AlgorithmType(Enum):
	BELLMAN_FORD = auto()
	DIJKSTRA = auto()
	KRUSKAL = auto()
	PRIMS = auto()
	KAHNS = auto()
	FLOYD_WARSHALL = auto()

class InputType(Enum):
	DICTIONARY = dict
	ADJACENCY_MATRIX = list

class Input(ABC):
	@abstractmethod
	def generate(self) -> list | dict:
		pass

class DijkstraInput(Input):
	def __init__(self, input_type):
		self.input_type = input_type
	def generate(self) -> list[list[int]] | dict[int, list]:
		match self.input_type:
			case InputType.DICTIONARY:
				return {
					0:[(4,1), (2,2)],
					1:[(3,2), (2,3), (3,4)],
					2:[(1,1), (4,3), (5,4)],
					3:[],
					4:[(1,3)],
				}
			case InputType.ADJACENCY_MATRIX:
				return [
					[0, 4, 2, 0, 0],
					[0, 0, 3, 2, 3],
					[0, 1, 0, 4, 5],
					[0, 0, 0, 0, 0],
					[0, 0, 0, 1, 0]
				]
			case _:
				raise ValueError("Invalid input type")

class BellmanFordInput(Input):
	def __init__(self, input_type):
		self.input_type = input_type
	def generate(self) -> list | dict:
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
				raise ValueError("Invalid input type")

class KruskalInput(Input):
	def __init__(self, input_type):
		self.input_type = input_type
	def generate(self) -> list | dict:
		match self.input_type:
			case InputType.DICTIONARY:
				return {
            		0: [(3, 3, 0), (3, 2, 0), (2, 1, 0)],
            		1: [(2, 0, 1), (4, 2, 1), (3, 4, 1)],
            		2: [(3, 0, 2), (5, 3, 2), (1, 4, 2), (4, 1, 2)],
            		3: [(3, 0, 3), (5, 2, 3), (7, 5, 3)],
            		4: [(8, 5, 4), (1, 2, 4), (3, 1, 4)],
            		5: [(9, 6, 5), (8, 4, 5), (7, 3, 5)],
            		6: [(9, 5, 6)],
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
				raise ValueError("Invalid input type")
			
class PrimsInput(Input):
	def __init__(self, input_type):
		self.input_type = input_type
	def generate(self) -> list | dict:
		match self.input_type:
			case InputType.DICTIONARY:
				return {
            		0: [(3, 3, 0), (3, 2, 0), (2, 1, 0)],
            		1: [(2, 0, 1), (4, 2, 1), (3, 4, 1)],
            		2: [(3, 0, 2), (5, 3, 2), (1, 4, 2), (4, 1, 2)],
            		3: [(3, 0, 3), (5, 2, 3), (7, 5, 3)],
            		4: [(8, 5, 4), (1, 2, 4), (3, 1, 4)],
            		5: [(9, 6, 5), (8, 4, 5), (7, 3, 5)],
            		6: [(9, 5, 6)],
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
				raise ValueError("Invalid input type")

class AbstractInputFactory(ABC):
	@abstractmethod
	def get_input(self, for_algorithm: AlgorithmType) -> list | dict:
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
				raise ValueError('Invalid input type')

class DictionaryInputFactory(AbstractInputFactory):
	@staticmethod
	def get_input(for_algorithm: AlgorithmType) -> list | dict:
		match for_algorithm:
			case AlgorithmType.DIJKSTRA:
				return DijkstraInput(InputType.DICTIONARY).generate()
			case AlgorithmType.BELLMAN_FORD:
				return BellmanFordInput(InputType.DICTIONARY).generate()
			case AlgorithmType.KRUSKAL:
				return KruskalInput(InputType.DICTIONARY).generate()
			case AlgorithmType.PRIMS:
				return PrimsInput(InputType.DICTIONARY).generate()
			case _:
				raise ValueError("Algorithm not supported")

class AdjacencyMatrixInputFactory(AbstractInputFactory):
	@staticmethod
	def get_input(for_algorithm: AlgorithmType) -> list | dict:
		match for_algorithm:
			case AlgorithmType.DIJKSTRA:
				return DijkstraInput(InputType.ADJACENCY_MATRIX).generate()
			case AlgorithmType.BELLMAN_FORD:
				return BellmanFordInput(InputType.ADJACENCY_MATRIX).generate()
			case AlgorithmType.KRUSKAL:
				return KruskalInput(InputType.ADJACENCY_MATRIX).generate()
			case AlgorithmType.PRIMS:
				return PrimsInput(InputType.ADJACENCY_MATRIX).generate()
			case _:
				raise ValueError("Algorithm not supported")

#####