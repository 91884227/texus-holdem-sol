import unittest
from Hand import Hand

class TestHand(unittest.TestCase):
    def setUp(self):
        print('setup')
        pass

    def tearDown(self):
        print('tearDown')
        pass


    def test_invalid_input(self):
        with self.assertRaises(Exception) as context:
            # wrong numbers of card
            Hand(["10c", "4h", "7d", "Kc", "2s", "3d"])

            # wrong number
            Hand(["10c", "4h", "7d", "Kc", "Ss"])

            # wrong suit
            Hand(["10c", "4h", "7d", "Kc", "2x"])
    
    def test_category(self):
        # base case
        self.assertEqual(Hand(["10c", "4h", "7d", "Kc", "2s"]).category, "high_card")
        self.assertEqual(Hand(["Kc",  "Kh", "7d", "2c", "5s"]).category, "pair")
        self.assertEqual(Hand(["Kc",  "Kh", "7d", "7c", "5s"]).category, "two_pair")
        self.assertEqual(Hand(["Kc",  "Kh", "Kd", "7c", "5s"]).category, "three_of_a_kind")
        self.assertEqual(Hand(["3c",  "4h", "5d", "6c", "7s"]).category, "straight")
        
        self.assertEqual(Hand(["3c",  "4c", "5c", "6c", "8c"]).category, "flush")
        self.assertEqual(Hand(["Kc",  "Kh", "Kd", "7c", "7s"]).category, "full_house")
        self.assertEqual(Hand(["6c",  "6h", "6d", "6s", "Ks"]).category, "full_of_a_kind")
        self.assertEqual(Hand(["10s", "Js", "Qs", "Ks", "1s"]).category, "straight_flush")

        # special case
        self.assertEqual(Hand(["1c",  "2h", "3d", "4c", "5s"]).category, "straight")
        self.assertEqual(Hand(["1d",  "2d", "3d", "4d", "5d"]).category, "straight_flush")

    def test_value(self):
        # base case
        self.assertEqual(Hand(["10c", "4h", "7d", "Kc", "2s"]).value, 11310070402)
        self.assertEqual(Hand(["Kc",  "Kh", "7d", "2c", "5s"]).value, 21307050200)
        self.assertEqual(Hand(["Kc",  "Kh", "7d", "7c", "5s"]).value, 31307050000)
        self.assertEqual(Hand(["Kc",  "Kh", "Kd", "7c", "5s"]).value, 41307050000)
        self.assertEqual(Hand(["3c",  "4h", "5d", "6c", "7s"]).value, 50700000000)
        
        self.assertEqual(Hand(["3c",  "4c", "5c", "6c", "8c"]).value, 60806050403)
        self.assertEqual(Hand(["Kc",  "Kh", "Kd", "7c", "7s"]).value, 71307000000)
        self.assertEqual(Hand(["6c",  "6h", "6d", "6s", "Ks"]).value, 80613000000)
        self.assertEqual(Hand(["10s", "Js", "Qs", "Ks", "1s"]).value, 91400000000)
        
        # another case
        self.assertEqual(Hand(["1c",  "2h", "3d", "4c", "5s"]).value, 50100000000)
        self.assertEqual(Hand(["1d",  "2d", "3d", "4d", "5d"]).value, 90100000000)
        
if __name__ == "__main__":
    unittest.main()