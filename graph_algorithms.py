from abc import ABC, abstractmethod
import input_factory
from input_factory import InputFactoryProducer, InputType, AlgorithmType
import solvers
from solvers import DijkstraSolver, BellmanFordSolver


class Algorithms(ABC):
	@abstractmethod
	def generate_input():
		pass
	@abstractmethod
	def solve():
		pass

class AlgorithmsFactory:
	@staticmethod
	def get_algorithm(algorithm_type: AlgorithmType) -> Algorithms:
		assert isinstance(algorithm_type, AlgorithmType)
		match algorithm_type:
			case AlgorithmType.DIJKSTRA:
				return Dijkstra()
			case AlgorithmType.BELLMAN_FORD:
				return BellmanFord()
			case AlgorithmType.KRUSKAL:
				return Kruskal()
			case _:
				return None

class Dijkstra(Algorithms):
	def __init__(self):
		self.input = None
		self.input_type = None
		self._input_factory = None
		self._solver = DijkstraSolver()

	def set_input_type(self, input_type: InputType) -> None:
		self.input_type = input_type
		self._input_factory = InputFactoryProducer.get_factory(self.input_type)
		self._solver.set_input_type(self.input_type)

	def generate_input(self) -> None:
		if not self.input_type:
			raise ValueError("An input type must be specified first")
		self.input = self._input_factory.get_input(AlgorithmType.DIJKSTRA)
		self._solver.set_graph(self.input)

	def solve(self, start: int) -> dict:
		assert self.input is not None and isinstance(start, int)
		return self._solver.solve(start)
	
	@staticmethod
	def solve_custom_input(graph):
		print("solving custom input")


class BellmanFord(Algorithms):
	def __init__(self):
		self.input = None
		self.input_type = None
		self._input_factory = None
		self._solver = BellmanFordSolver()

	def set_input_type(self, input_type: InputType) -> None:
		self.input_type = input_type
		self._input_factory = InputFactoryProducer.get_factory(self.input_type)
		self._solver.set_input_type(self.input_type)

	def generate_input(self) -> None:
		if not self.input_type:
			raise ValueError("An input type must be specified first")
		self.input = self._input_factory.get_input(AlgorithmType.BELLMAN_FORD)
		self._solver.set_graph(self.input)

	def solve(self, start: int) -> dict:
		assert self.input is not None and isinstance(start, int)
		return self._solver.solve(start)
	
	@staticmethod
	def solve_custom_input(graph):
		print("solving custom input")


class Kruskal(Algorithms):
	def __init__(self):
		self.graph = None

	def generate_input(self, input_type: InputType) -> None:
		assert isinstance(input_type, InputType)
		_factory = InputFactoryProducer.get_factory(input_type)
		self.graph = _factory.get_input(AlgorithmType.KRUSKAL)

	def solve(self, start: int) -> dict:
		assert self.graph is not None and isinstance(start, int)
		match type(self.graph):
			case InputType.DICTIONARY.value:
				print("solving dict")
			case InputType.ADJACENCY_MATRIX.value:
				print("Solving matrix")
			case _:
				print("Other")
	@staticmethod
	def solve_custom_input(graph):
		print("solving custom input")