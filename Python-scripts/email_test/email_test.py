# test the function email_test.py
import unittest

from emails import find_email

class EmailsTest(unittest.TestCase):
    def test_basic(self):
        testcase = [None, 'Blossom', 'Gill']
        expected = 'blossom@abc.edu'
        self.assertEqual(find_email(testcase), expected)
    # def test_one_name(self):
    #     testcase = [ 'John', 'Doe' ]
    #     expected = 'Missing parameters'
    #     self.assertEqual(find_email(testcase), expected)

if __name__ == '__main__':
    unittest.main()
