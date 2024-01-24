import unittest
from stage2 import Student, is_valid_name, is_valid_email, main
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student('John', 'Doe', 'john.doe@example.com')

    def test_repr(self):
        self.assertEqual(repr(
            self.student), "Student(first_name='John', last_name='Doe', email='john.doe@example.com')")


class TestValidations(unittest.TestCase):

    def test_is_valid_name(self):
        self.assertTrue(is_valid_name('John Doe'))
        self.assertFalse(is_valid_name('John123'))
        self.assertTrue(is_valid_name('John Doe jdoe@mail.net'))  # new test
        self.assertTrue(is_valid_name(
            'Mary Luise Johnson maryj@google.com'))  # new test

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email('john.doe@example.com'))
        self.assertFalse(is_valid_email('john.doe@example'))
        self.assertTrue(is_valid_email('jdoe@mail.net'))  # new test
        self.assertTrue(is_valid_email('maryj@google.com'))  # new test


class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['add students', 'John Doe jdoe@mail.net', 'back', 'exit'])
    def test_main(self, input_mock):
        students = main()
        self.assertEqual(len(students), 1)
        self.assertIsInstance(students[0], Student)
        self.assertEqual(students[0].first_name, 'John')
        self.assertEqual(students[0].last_name, 'Doe')
        self.assertEqual(students[0].email, 'jdoe@mail.net')


if __name__ == '__main__':
    unittest.main()
