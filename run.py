import graph_algorithms
from graph_algorithms import AlgorithmsFactory
import input_factory
from input_factory import InputType, AlgorithmType

def main():
	p = AlgorithmsFactory.get_algorithm(AlgorithmType.PRIMS)
	p.set_input_type(InputType.ADJACENCY_MATRIX)
	p.generate_input()
	print(p.solve(start=0))

if __name__=="__main__":
	main()
