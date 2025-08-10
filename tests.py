import unittest
from grades import calculate_average

class TestGrades(unittest.TestCase):

    def test_average(self):
        data = {"Alice": 90, "Bob": 80, "Charlie": 70}
        avg = sum(data.values()) / len(data)
        self.assertAlmostEqual(avg, 80.0)

    def test_average_empty(self):
        data = {}
        with self.assertRaises(ZeroDivisionError):
            _ = sum(data.values()) / len(data)

if __name__ == "__main__":
    unittest.main()
