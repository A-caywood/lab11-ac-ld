#https://github.com/A-caywood/lab11-ac-ld
#Partner 1: Andrew Caywood
#Partner 2: Liam Dombrowski
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
   def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(1, -8), -8)
        self.assertEqual(multiply(0, 6), 0)

   def test_divide(self):
       self.assertEqual(divide(2, 6), 3.0)
       self.assertEqual(divide(2, 5), 2.5)
       self.assertEqual(divide(4, -8), -2.0)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
<<<<<<< HEAD
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)
=======
>>>>>>> 63a72346b1f6a1fdea5a7b04611dcc4635e0ad05

   ######## Partner 1
   def test_log_invalid_argument(self):
    with self.assertRaises(ValueError):
        logarithm(2, 0)

   def test_hypotenuse(self):
    self.assertEqual(hypotenuse(3, 4), 5.0)
    self.assertEqual(hypotenuse(0, 0), 0.0)
    self.assertEqual(hypotenuse(5, 12), 13.0)


   def test_sqrt(self):
    with self.assertRaises(ValueError):
        square_root(-9)
    self.assertEqual(square_root(9), 3.0)
    self.assertEqual(square_root(0), 0.0)
    ##########################


    #Partner 2
   def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-202,202), 0)
        self.assertEqual(add(-1000, -1000), -2000)
   def test_subtract(self):
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(100,100), 0)
        self.assertEqual(sub(-200, -201), 1)
   def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,2)
        with self.assertRaises(ZeroDivisionError):
            div(0, 999999)
   def test_logarithm(self):
        self.assertEqual(log(2, 9), math.log(9, 2))
        self.assertEqual(log(10,1000), math.log(1000, 10))
        self.assertEqual(log(10,1), 0)
   def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(0, 10)
        with self.assertRaises(ValueError):
            log(10,0)
        with self.assertRaises(ValueError):
            log(0,0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()