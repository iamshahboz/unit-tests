import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(40,10),30)
        self.assertEqual(calc.subtract(-15,-5),-10)
        self.assertEqual(calc.subtract(-1,-1),0)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(4,8),32)
        self.assertEqual(calc.multiply(-5,1),-5)
        self.assertEqual(calc.multiply(-1,-1),1)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)

        #this is one method of rising erros
        #self.assertRaises(ValueError,calc.divide,10,0) 

        #this is another one
        with self.assertRaises(ValueError):
            calc.divide(10,3) 



    
if __name__ == '__main__':
    unittest.main()


