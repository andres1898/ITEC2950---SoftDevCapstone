from unittest import TestCase
import unittest

import quiz


class Test_check_answer(TestCase):
    def test_check_answer_True(self):
        # Arrange
        correct_answer = 'Saturn'
        user_answer = 'Saturn'

        # Action
        result = quiz.check_answer(correct_answer, user_answer)

        #Assert
        self.assertEqual(result, True)

    def test_check_answer_even_with_spaces(self):
        # Arrange
        correct_answer = 'Saturn'
        user_answer = ' Saturn '

        # Action
        result = quiz.check_answer(correct_answer, user_answer)

        #Assert
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()