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
    def test_output_type(self):
        # adj matrix input case
        b1 = AlgorithmsFactory.get_algorithm(AlgorithmType.BELLMAN_FORD)
        b1.set_input_type(InputType.ADJACENCY_MATRIX) # type: ignore
        b1.generate_input()
        # dict input case 
        b2 = AlgorithmsFactory.get_algorithm(AlgorithmType.BELLMAN_FORD)
        b2.set_input_type(InputType.DICTIONARY) # type: ignore
        b2.generate_input()

        r1, r2 = b1.solve(0), b2.solve(0)
        assert isinstance(r1, dict) and isinstance(r2, dict)
    
    def test_input_consistency(self):
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

class KruskalTests(unittest.TestCase):
    def test_output_type(self):
        # adj matrix input case
        k1 = AlgorithmsFactory.get_algorithm(AlgorithmType.KRUSKAL)
        k1.set_input_type(InputType.ADJACENCY_MATRIX) # type: ignore
        k1.generate_input()
        # dict input case 
        k2 = AlgorithmsFactory.get_algorithm(AlgorithmType.KRUSKAL)
        k2.set_input_type(InputType.DICTIONARY) # type: ignore
        k2.generate_input()

        r1, r2 = k1.solve(0), k2.solve(0)
        assert isinstance(r1, list) and isinstance(r2, list)
    
    def test_input_consistency(self):
        k1 = AlgorithmsFactory.get_algorithm(AlgorithmType.KRUSKAL)
        k1.set_input_type(InputType.ADJACENCY_MATRIX)
        k1.generate_input()
        
        k2 = AlgorithmsFactory.get_algorithm(AlgorithmType.KRUSKAL)
        k2.set_input_type(InputType.DICTIONARY)
        k2.generate_input()

        r1, r2 = k1.solve(0), k2.solve(0)
        assert r1 == r2

class PrimsTests(unittest.TestCase):
    def test_output_type(self):
        # adj matrix input case
        p1 = AlgorithmsFactory.get_algorithm(AlgorithmType.PRIMS)
        p1.set_input_type(InputType.ADJACENCY_MATRIX) # type: ignore
        p1.generate_input()
        # dict input case 
        p2 = AlgorithmsFactory.get_algorithm(AlgorithmType.PRIMS)
        p2.set_input_type(InputType.DICTIONARY) # type: ignore
        p2.generate_input()

        r1, r2 = p1.solve(0), p2.solve(0)
        assert isinstance(r1, list) and isinstance(r2, list)
    
    def test_input_consistency(self):
        p1 = AlgorithmsFactory.get_algorithm(AlgorithmType.PRIMS)
        p1.set_input_type(InputType.ADJACENCY_MATRIX)
        p1.generate_input()
        
        p2 = AlgorithmsFactory.get_algorithm(AlgorithmType.PRIMS)
        p2.set_input_type(InputType.DICTIONARY)
        p2.generate_input()

        r1, r2 = p1.solve(0), p2.solve(0)
        assert r1 == r2

if __name__=="__main__":
    unittest.main()