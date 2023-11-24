import unittest

class CrmTest(unittest.TestCase):
    def test_1_2(self):
        result = 1 + 2
        # Assert
        self.assertEqual(result, 3)

    def test_2_2(self):
        result = 2 + 2
        # Assert
        self.assertEqual(result, 4)

# unittest.main()