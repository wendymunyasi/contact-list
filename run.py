#!/usr/bin/env python3.6

from contact import Contact


def create_contact(fname, lname, phone, email):

    new_contact = Contact(fname, lname, phone, email)
    return new_contact


def save_contacts(contact):

    contact.save_contact()


def del_contact(contact):

    contact.delete_contact()


def find_contact(number):
    return Contact.find_by_number(number)


def check_existing_contacts(number):
    return Contact.contact_exists(number)


def display_contacts():
    return Contact.display_contacts()


def main():

    print("Hello Welcome to your contact list. What is your name?")

    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Use these three short codes : cc - create a new contact, dc - display contact. fc - find contact, ex - exit the contact list, del - delete contact, ex - exit ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Contact")
            print("-"*10)

            print("First name ...")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            save_contacts(create_contact(f_name, l_name, p_number, e_address))
            print('\n')
            print(f"New Contact {f_name} {l_name} created")
            print('\n')

        elif short_code == 'dc':

            if display_contacts():
                print("Here is a list of all your contacts")
                print('\n')

                for contact in display_contacts():
                    print(f"{contact.first_name} ....{contact.last_name}")

                    print('\n')
            else:
                print('\n')
                print("You don't seem to have any contacts saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the number you want to search for")

            search_number = input()

            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print('-' * 20)

                print(f"Phone number.......{search_contact.phone_number}")
                print(f"Email address.......{search_contact.email}")
            else:
                print("That contact does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break

        elif short_code == "del":
            print("Are you sure you want to delete contact? Input y or n")

            answer = input().lower()

            if answer == 'y':
                print("Enter the number of the contact you want to delete")

                searched_number = input()

                if check_existing_contacts(searched_number):
                    searched_contact = find_contact(searched_number)
                    print(
                        f"{searched_contact.first_name} {searched_contact.last_name}")
                    print('-' * 20)

                    print(
                        f"Phone number.......{searched_contact.phone_number}")
                    print(f"Email address.......{searched_contact.email}")

                    print('\n')
                    print(" Is this the contact you want to delete? Type y or n.")

                    answer_two = input()

                    if answer_two == 'y':
                        searched_contact.delete_contact()
                    else:
                        print('\n')

                else:
                    print("That contact does not exist")

            else:
                print('\n')

        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
