import graph_algorithms
from graph_algorithms import AlgorithmsFactory
import input_factory
from input_factory import InputType, AlgorithmType
import unittest

class DijkstraTests(unittest.TestCase):
    def test_output_type(self):
        # adj matrix input case
        d1 = AlgorithmsFactory.get_algorithm(AlgorithmType.DIJKSTRA)
        d1.set_input_type(InputType.ADJACENCY_MATRIX) # type: ignore
        d1.generate_input()
        # dict input case 
        d2 = AlgorithmsFactory.get_algorithm(AlgorithmType.DIJKSTRA)
        d2.set_input_type(InputType.DICTIONARY) # type: ignore
        d2.generate_input()

        assert isinstance(d1.solve(0), dict ) and isinstance(d2.solve(0), dict)

    def test_input_consistency(self):
        d1 = AlgorithmsFactory.get_algorithm(AlgorithmType.DIJKSTRA)
        d1.set_input_type(InputType.ADJACENCY_MATRIX) # type: ignore
        d1.generate_input()
        
        d2 = AlgorithmsFactory.get_algorithm(AlgorithmType.DIJKSTRA)
        d2.set_input_type(InputType.DICTIONARY) # type: ignore
        d2.generate_input()

        r1, r2 = d1.solve(0), d2.solve(0)
        assert isinstance(r1, dict) and isinstance(r2, dict)

        for k, v in r1.items():
            assert r2[k] == v

class BellmanFordTests(unittest.TestCase):
    def test_bellman_ford_input_consistency(self):
        b1 = AlgorithmsFactory.get_algorithm(AlgorithmType.BELLMAN_FORD)
        b1.set_input_type(InputType.ADJACENCY_MATRIX)
        b1.generate_input()
        
        b2 = AlgorithmsFactory.get_algorithm(AlgorithmType.BELLMAN_FORD)
        b2.set_input_type(InputType.DICTIONARY)
        b2.generate_input()

        r1, r2 = b1.solve(0), b2.solve(0)
        assert isinstance(r1, dict) and isinstance(r2, dict)
        
        for k, v in r1.items():
            assert r2[k] == v

if __name__=="__main__":
    unittest.main()