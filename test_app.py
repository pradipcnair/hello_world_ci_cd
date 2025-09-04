#test app.py
import unittest
from app import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def test_HelloWorld(self):
        self.assertEqual(HelloWorld(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()

