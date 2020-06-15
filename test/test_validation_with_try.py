import unittest



class MyTestCase(unittest.TestCase):
    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)


if __name__ == '__main__' :
    unittest.main()
