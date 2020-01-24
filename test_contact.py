import unittest
import pyperclip
from contact import Contact

class TestContact(unittest.TestCase):

    def tearDown(self):

        Contact.contact_list = []

    def setUp(self):

        self.new_contact = Contact(
            "James", "Muriuki", "0712345678", "james@ms.com")

    def test_init(self):

        self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "0712345678")
        self.assertEqual(self.new_contact.email, "james@ms.com")

    def test_save_contact(self):
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def test_save_multiple_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678",
                               "test@user.com")                  # new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_contact(self):

        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678",
                               "test@user.com")  # new contact
        test_contact.save_contact()

        self.new_contact.delete_contact()  # Deleting a contact object
        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact_by_number(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711223355", "test@user.com")
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711223355")

        self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exists(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711223355", "test@user.com")
        test_contact.save_contact()

        contact_exists = Contact.contact_exists("0711223355")

        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        self.assertEqual(Contact.display_contacts(), Contact.contact_list)

    def test_copy_email(self):
        self.new_contact.save_contact()
        Contact.copy_email("0712345678")

        self.assertEqual(self.new_contact.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
