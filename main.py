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
            return "Not enough params or wrong phone format"

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
            raise ValueError

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
        raise ValueError

    def edit_phone(self, old_phone, new_phone):
        found = False
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                phone.validate_phone()
                found = True
                break

        if not found:
            raise ValueError 

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        
    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())


def main():

    while True:
        user_input = input(">>>: ")

        if user_input.lower() in ["exit", "close", "good bye"]:
            print("Goodbye!")
            break
        else:
            handler, arguments = parser(user_input)
            print(handler(*arguments))


def parser(user_input: str):
    COMMANDS = {
        "Hello": hello_func,
        "Add": add_func,
        "Change": change_func,
        "Phone": search_func,
        "Show All": show_func,
        "Del": delete_func
    }

    user_input = user_input.title()

    for kw, command in COMMANDS.items():
        if user_input.startswith(kw):
            return command, user_input[len(kw):].strip().split()
    return unknown_command, []


@deco_error
def add_func(*args):
    name = args[0]
    record = Record(name)
    phone_numbers = args[1:]
    for phone_number in phone_numbers:
        record.add_phone(phone_number)
    address_book.add_record(record)
    return f"User {name} has been added to the phone book with phone number(s) {', '.join(phone_numbers)}"


@deco_error
def change_func(*args):
    name = args[0]
    phone_numbers = args[1:]
    record = address_book.find(name)
    if record:
        for phone in phone_numbers:
            record.edit_phone(phone, phone)
        return f"Phone number for user {name} has been changed to {', '.join(phone_numbers)}"
    else:
        raise KeyError
    

@deco_error
def delete_func(*args):
    name = args[0]
    address_book.delete(name)
    return f"User {name} has been deleted from the phone book"


@deco_error
def search_func(*args):
    name = args[0]
    record = address_book.find(name)
    if record:
        return str(record)
    else:
        raise KeyError


@deco_error
def show_func(*args):
    return str(address_book)


def unknown_command():
    return "Unknown command. Try again."


def hello_func():
    return "How can I help you?"


address_book = AddressBook()


if __name__ == '__main__':
    main()
