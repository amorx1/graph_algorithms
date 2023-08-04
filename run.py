import graph_algorithms
from graph_algorithms import AlgorithmsFactory
import input_factory
from input_factory import InputType, AlgorithmType

def main():
	k = AlgorithmsFactory.get_algorithm(AlgorithmType.KRUSKAL)
	k.set_input_type(InputType.DICTIONARY)
	k.generate_input()
	print(k.solve(start=0))

if __name__=="__main__":
	main()
