
import unittest
from unittest.mock import patch
from empoyee_class import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee('Jack','Jones',40000)
        self.emp2 = Employee('Eddy','Kenzo',70000)
        
    def tearDown(self): 
        pass


    def test_email(self):

        self.assertEqual(self.emp1.email,'Jack.Jones@email.com')
        self.assertEqual(self.emp2.email,'Eddy.Kenzo@email.com')

        self.emp1.first = 'John'
        self.emp2.first='Jane'

        self.assertEqual(self.emp1.email,'John.Jones@email.com')
        self.assertEqual(self.emp2.email,'Jane.Kenzo@email.com')

    def test_fullname(self):

        self.assertEqual(self.emp1.full_name,'Jack Jones')
        self.assertEqual(self.emp2.full_name,'Eddy Kenzo')

        self.emp1.first = 'John'
        self.emp2.first='Jane'

        self.assertEqual(self.emp1.full_name,'John Jones')
        self.assertEqual(self.emp2.full_name,'Jane Kenzo')

    def test_apply_raise(self):

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay,42000)
        self.assertEqual(self.emp2.pay,73500)

    def test_monthly_schedule(self):
        with patch('empoyee_class.requests.get') as mocked_get:
            mocked_get.return_value.ok= True
            mocked_get.return_value.text="Success"

            schedule = self.emp1.monthly_schedule("May")
            mocked_get.assert_called_with('http://company.com/Jones/May')
            self.assertEqual(schedule,"Success")

            mocked_get.return_value.ok= False
            

            schedule = self.emp2.monthly_schedule("June")
            mocked_get.assert_called_with('http://company.com/Kenzo/June')
            self.assertEqual(schedule,"Bad response")


if __name__ == '__main__':
    unittest.main()


        





