import unittest
import missingletters

class TestMissingLetters (unittest.TestCase):

    def test_noletters(self):
        self.assertEqual('abcdefghijklmnopqrstuvwxyz', missingletters.processLine(''))

    def test_allletters(self):
        self.assertEqual('', missingletters.processLine('abcdefghijklmnopqrstuvwxyz'))

    def test_missingsome_and_noalpha(self):
        self.assertEqual('anz', missingletters.processLine('bcdefghijklm  % & * opqrstuvwxy'))

if __name__ == '__main__':
    unittest.main()

