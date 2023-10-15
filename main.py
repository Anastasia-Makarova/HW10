from collections import UserDict



def deco_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params"
        except KeyError:
            return f"There is no contact such in phone book. Please, use command 'Add...' first"
        except ValueError:
            return "Not enough params"

    return inner

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        if not self.value.isdigit() or len(self.value) != 10:
            raise ValueError("Некоректний формат телефону")

    def __str__(self):
        return str(self.value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError(f"Номер телефону {phone} не існує")

    def edit_phone(self, old_phone, new_phone):
        found = False
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                phone.validate_phone()
                found = True
                break

        if not found:
            raise ValueError(f"Номер телефону {old_phone} не існує")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(map(str, self.phones))}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


def main():
    address_book = AddressBook()

    while True:
        user_input = input(">>>: ")

        if user_input.lower() in ["exit", "close", "good bye"]:
            print("Goodbye!")
            break
        else:
            handler, arguments = parser(user_input, address_book)
            print(handler(*arguments))


def parser(user_input: str, address_book: AddressBook):
    COMMANDS = {
        "Hello": hello_func,
        "Add": add_func,
        "Change": change_func,
        "Phone": search_func,
        "Show All": show_func
    }

    user_input = user_input.title()

    for kw, command in COMMANDS.items():
        if user_input.startswith(kw):
            return command, user_input[len(kw):].strip().split(), address_book
    return unknown_command, []


@deco_error
def add_func(*args, address_book: AddressBook):
    name = args[0]
    record = Record(name)
    for phone_number in args[1:]:
        record.add_phone(phone_number)
    address_book.add_record(record)
    return f"User {name} has been added to the phone book with phone number(s) {', '.join(args[1:])}"


@deco_error
def change_func(*args, address_book: AddressBook):
    name = args[0]
    phone = args[1]
    record = address_book.find(name)
    if record:
        record.edit_phone(phone)
        return f"Phone number for user {name} has been changed to {phone}"
    else:
        raise KeyError(f"No contact found for {name}")


@deco_error
def search_func(*args, address_book: AddressBook):
    name = args[0]
    record = address_book.find(name)
    if record:
        return str(record)
    else:
        raise KeyError(f"No contact found for {name}")


@deco_error
def show_func(*args, address_book: AddressBook):
    return str(address_book)


def unknown_command():
    return "Unknown command. Try again."


def hello_func():
    return "How can I help you?"


if __name__ == '__main__':
    main()
