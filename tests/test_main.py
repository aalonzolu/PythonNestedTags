from unittest import TestCase
from src.main import check_nested


class TestMain(TestCase):
    def test_nested_valid(self):
        s = "{[()()]}"
        result = check_nested(s)
        self.assertEqual(1, result)

    def test_invalid_nested(self):
        s = "({)()]"
        result = check_nested(s)
        self.assertEqual(0, result)
