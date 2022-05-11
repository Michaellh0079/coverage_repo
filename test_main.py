import unittest

from main import function_a, function_b


class TestMain(unittest.TestCase):

    def test_function_a(self):
        function_a()
        pass

    def test_function_b(self):
        function_b()
        pass
