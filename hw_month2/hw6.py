class Contact:
    def __init__(self, name, phone_number, contact_id):
        self.name = name
        self.phone_number = phone_number
        self.id = contact_id

    @staticmethod
    def validate_phone_num(phone_number):
        return len(phone_number) == 10 and phone_number.isdigit()

    def __str__(self):
        return f"Имя: {self.name}, номер: {self.phone_number}, ID: {self.id}"


class ContactList:
    last_id = 0

    def __init__(self):
        self.all_contacts = []

    def add_contact(self, name, phone_number):
        if not Contact.validate_phone_num(phone_number):
            print("Номер должен состоять из 10 цифр.")
            return
        for contact in self.all_contacts:
            if contact.phone_number == phone_number:
                print(f"Контакт уже добавлен: {contact}")
                return

        ContactList.last_id += 1
        new_contact = Contact(name, phone_number, ContactList.last_id)
        self.all_contacts.append(new_contact)
        print(f"Добавлен контакт: {new_contact}")

    def show_all(self):
        if not self.all_contacts:
            print("Список контактов пуст.")
        else:
            print("\nВсе контакты:")
            for c in self.all_contacts:
                print(c)

    def remove_contact_by_id(self, contact_id=None):
        if contact_id is None:
            try:
                contact_id = int(input("Введите ID контакта, который нужно удалить: "))
            except ValueError:
                print("Некорректный ввод. ID должен быть числом.")
                return

        for i, contact in enumerate(self.all_contacts):
            if contact.id == contact_id:
                removed = self.all_contacts.pop(i)
                print(f"Контакт удалён: {removed}")
                return

        print(f"Контакт с ID {contact_id} не найден.")


#
contacts = ContactList()
contacts.add_contact("Нурбол", "7768784844")
contacts.add_contact("Айда", "7700123456")
contacts.add_contact("Самат", "7768787556")
contacts.show_all()
print(f"ПОСЛЕДНИЙ ID: {ContactList.last_id}")


contacts.remove_contact_by_id()
contacts.show_all()





