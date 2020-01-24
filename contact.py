import pyperclip

class Contact:

    contact_list = []  # Empty contact list

    def __init__(self, first_name, last_name, number, email):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

    def save_contact(self):
        Contact.contact_list.append(self)

    def delete_contact(self):
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls, number):
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exists(cls, number):
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True
        return False

    @classmethod
    def display_contacts(cls):
        return cls.contact_list

    @classmethod
    def display_all_contacts(cls):
        return cls.contact_list

    @classmethod
    def copy_email(cls, number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
