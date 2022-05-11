import unittest
import main
from unittest.mock import patch

class TestMain(unittest.TestCase):


    def test_profitMaximization(self):
        pass

    @patch('yourmodule.get_input', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(run, 'you entered yes')

    def test_monopolySolver(self):
        pass
