#!/usr/bin/env python3
import unittest

def validate_user(username, minlen):
    assert type(username) == str, 'username must be a string'
    if minlen < 1:
        raise ValueError('minlen must be at least 1')
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

#print(validate_user("blue", 5)) # False
#print(validate_user(88, 5)) # AssertionError
##print(validate_user("blue", -1)) # ValueError

class TestValidateUser(unittest.TestCase):
  def test_valid(self):
    self.assertEqual(validate_user("validuser", 3), True)

  def test_too_short(self):
    self.assertEqual(validate_user("inv", 5), False)

  def test_invalid_characters(self):
    self.assertEqual(validate_user("invalid_user", 1), False)
  def test_invalid_minlen(self):
    self.assertRaises(ValueError, validate_user, "user", -1)

if __name__ == '__main__':
    unittest.main()