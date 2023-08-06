from abc import ABC, abstractmethod
from ctypes import Union
from typing import Optional
from typing_extensions import override
import input_factory
from input_factory import AbstractInputFactory, Input, InputFactoryProducer, InputType, AlgorithmType
import solvers
from solvers import DijkstraSolver, BellmanFordSolver, KruskalSolver, PrimsSolver


class Algorithms(ABC):
	@abstractmethod
	def set_input_type(self, input_type: InputType) -> None:
		pass
	@abstractmethod
	def generate_input():
		pass
	@abstractmethod
	def solve(self, start: int) -> list | dict | int:
		pass
	@abstractmethod
	def draw_solution():
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
			case AlgorithmType.PRIMS:
				return Prims()
			case _:
				raise ValueError("Invalid algorithm type")


class Dijkstra(Algorithms):
	def __init__(self):
		self.input: Optional[list | dict] = None
		self.input_type: Optional[InputType] = None
		self._input_factory: Optional[AbstractInputFactory] = None
		self._solver = DijkstraSolver()

	def set_input_type(self, input_type: InputType) -> None:
		self.input_type = input_type
		self._input_factory = InputFactoryProducer.get_factory(self.input_type)
		self._solver.set_input_type(self.input_type)

	def generate_input(self) -> None:
		assert isinstance(self.input_type, InputType) and isinstance(self._input_factory, AbstractInputFactory)
		self.input = self._input_factory.get_input(AlgorithmType.DIJKSTRA)
		self._solver.set_graph(self.input)

	def solve(self, start: int) -> list | dict:
		assert self.input is not None and isinstance(start, int)
		return self._solver.solve(start)
	
	@staticmethod
	def solve_custom_input(graph):
		print("solving custom input")
	
	@staticmethod
	def draw_solution(res):
		pass


class BellmanFord(Algorithms):
	def __init__(self):
		self.input: Optional[list | dict] = None
		self.input_type: Optional[InputType] = None
		self._input_factory: Optional[AbstractInputFactory] = None
		self._solver = BellmanFordSolver()

	def set_input_type(self, input_type: InputType) -> None:
		self.input_type = input_type
		self._input_factory = InputFactoryProducer.get_factory(self.input_type)
		self._solver.set_input_type(self.input_type)

	def generate_input(self) -> None:
		assert isinstance(self.input_type, InputType) and isinstance(self._input_factory, AbstractInputFactory)
		self.input = self._input_factory.get_input(AlgorithmType.BELLMAN_FORD)
		self._solver.set_graph(self.input)

	def solve(self, start: int) -> list | dict:
		assert self.input is not None and isinstance(start, int)
		return self._solver.solve(start)
	
	@staticmethod
	def solve_custom_input(graph):
		print("solving custom input")

	@staticmethod
	def draw_solution(res):
		pass


class Kruskal(Algorithms):
	def __init__(self):
		self.input: Optional[list | dict] = None
		self.input_type: Optional[InputType] = None
		self._input_factory: Optional[AbstractInputFactory] = None
		self._solver = KruskalSolver()

	def set_input_type(self, input_type: InputType) -> None:
		self.input_type = input_type
		self._input_factory = InputFactoryProducer.get_factory(self.input_type)
		self._solver.set_input_type(self.input_type)

	def generate_input(self) -> None:
		assert isinstance(self.input_type, InputType) and isinstance(self._input_factory, AbstractInputFactory)
		self.graph = self._input_factory.get_input(AlgorithmType.KRUSKAL)
		self._solver.set_graph(self.graph)

	def solve(self, start: int) -> list | dict:
		assert self.graph is not None and isinstance(start, int)
		return self._solver.solve(start)

	@staticmethod
	def solve_custom_input(graph):
		print("solving custom input")
	
	@staticmethod
	def draw_solution(res):
		pass

class Prims(Algorithms):
	def __init__(self):
		self.input: Optional[list | dict] = None
		self.input_type: Optional[InputType] = None
		self._input_factory: Optional[AbstractInputFactory] = None
		self._solver = PrimsSolver()

	def set_input_type(self, input_type: InputType) -> None:
		self.input_type = input_type
		self._input_factory = InputFactoryProducer.get_factory(self.input_type)
		self._solver.set_input_type(self.input_type)

	def generate_input(self) -> None:
		assert isinstance(self.input_type, InputType) and isinstance(self._input_factory, AbstractInputFactory)
		self.graph = self._input_factory.get_input(AlgorithmType.PRIMS)
		self._solver.set_graph(self.graph)

	def solve(self, start: int) -> list | dict:
		assert self.graph is not None and isinstance(start, int)
		return self._solver.solve(start)

	@staticmethod
	def solve_custom_input(graph):
		print("solving custom input")
	
	@staticmethod
	def draw_solution(res):
		pass