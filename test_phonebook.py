import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    # def tearDown(self) -> None:
    #     pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing_name")

    # @unittest.skip("WIP")
    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_duplicate_entries(self):
        self.phonebook.add("Steve", "012345")
        self.phonebook.add("Sue", "012345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_is_consistent_with_duplicate_prefix(self):
        self.phonebook.add("Steve", "12345")
        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Sue", "12345")
        self.assertIn("Sue", self.phonebook.get_names())
        self.assertIn("12345", self.phonebook.get_phone_number())

# arrange
# act
# assert


if __name__ == '__main__':
    unittest.main()
