import unittest
import String_prossecor


class TestStringProcessor(unittest.TestCase):

    def test_reverse_string(self):
        result = String_prossecor.reverse_string("hello")
        self.assertEqual(result, "olleh")

    def test_reverse_empty(self):
        result = String_prossecor.reverse_string("")
        self.assertEqual(result, "")

    def test_count_vowels(self):
        result = String_prossecor.count_vowels("education")
        self.assertEqual(result, 5)

    def test_no_vowels(self):
        result = String_prossecor.count_vowels("rhythm")
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()