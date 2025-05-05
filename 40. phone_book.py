import json


class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def get_first_letter(self):
        return self.name[0]

    def __str__(self):
        return f"Name: {self.name}, Number: {self.phone_number}"


class PhoneBook:
    def __init__(self):
        self.contact_list = dict()

    def add_contact(self):
        name = input("Enter Name: ")
        number = input("Enter Number: ")
        contact = Contact(name, number)

        key = contact.get_first_letter()
        if self.contact_list.get(key) is None:
            self.contact_list[key] = list([contact])
        else:
            contacts = self.contact_list[key]
            contacts.append(contact)

        self.save()

    def show_contacts(self):
        try:
            fp = open("phone_book.json", "r")
            phone_book_json = fp.read()
            self.contact_list = json.loads(phone_book_json)
            fp.close()
        except:
            print("Empty phone book.")

        if len(self.contact_list) > 0:
            for key in iter(self.contact_list.keys()):
                print(f"Contacts starting with: {key}")
                for contact in self.contact_list[key]:
                    print("\t", Contact(**contact))

    def save(self):
        fp = open("phone_book.json", "w")
        fp.write(json.dumps(self.contact_list, default=converter))
        fp.close


def converter(obj):
    if isinstance(obj, Contact):
        return {"name": obj.name, "phone_number": obj.phone_number}


phone_book = PhoneBook()
phone_book.show_contacts()

print("\nPlease choose from the following:")
while True:
    ip = input("Type add/show/exit: ")
    if ip == "add":
        phone_book.add_contact()
    elif ip == "show":
        phone_book.show_contacts()
    if ip == "exit":
        phone_book.save()
        break
