import unittest
import ezr
from ezr import the, DATA, csv, dot
import random
from extend import process_data, guess

class TestExtend(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.train = "/workspaces/ezr/data/optimize/config/SS-A.csv"
        self.d = DATA().adds(csv(self.train))
    
    def test_shuffle_jiggles_order(self):
        original_order = self.d.rows.copy()
        self.d.shuffle()
        shuffled_order = self.d.rows
        self.assertNotEqual(original_order, shuffled_order, "Shuffle did not change the order of the data")

    def test_chebyshevs_top_item(self):
        some = random.choices(self.d.rows, k=10)
        sorted_rows = self.d.clone().adds(some).chebyshevs().rows
        top_item = sorted_rows[0]
        self.assertEqual(top_item, min(sorted_rows, key=lambda row: self.d.chebyshev(row)), "Top item is not the smallest in chebyshev sort")

    def test_smart_and_dumb_list_lengths(self):
        N = 30
        sample_size = 20
        
        # Test dumb list length
        dumb = [guess(N, self.d) for _ in range(N)]
        self.assertEqual(len(dumb), N, "Dumb list length is not equal to N")
        
        # Test smart list length
        smart = [self.d.shuffle().activeLearning() for _ in range(N)]
        self.assertEqual(len(smart), N, "Smart list length is not equal to N")

if __name__ == '__main__':
    unittest.main()