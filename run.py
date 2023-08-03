import graph_algorithms
from graph_algorithms import AlgorithmsFactory, Dijkstra, BellmanFord, Kruskal
import input_factory
from input_factory import InputType, AlgorithmType

def main():
	dijkstra = AlgorithmsFactory.get_algorithm(AlgorithmType.DIJKSTRA)
	dijkstra.set_input_type(InputType.ADJACENCY_MATRIX)
	dijkstra.generate_input()
	print(dijkstra.solve(start=0))

if __name__=="__main__":
	main()
