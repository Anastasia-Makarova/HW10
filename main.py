from collections import UserDict

class Field:
    def desc():
        ...
        # Базовий клас для полів запису. Буде батьківським для всіх полів, у ньому реалізується логіка загальна для всіх полів

        # + 1. Класс Field в коді оголошено
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):

    def desc():
        ...
        # Клас для зберігання імені контакту. Обов'язкове поле.
        # + 2. Класс Name в коді оголошено
        # + 3. Класс Name наслідується від класу Field в коді

    
    def __init__(self, value: str) -> None:
        self.name = value


class Phone(Field):
    def desc():
        ...
        # Клас для зберігання номера телефону. Має валідацію формату (10 цифр). \\\
        # Необов'язкове поле з телефоном та таких один запис Record може містити декілька.

        # Критерії приймання:
            # Реалізовано валідацію номера телефону (має бути 10 цифр).

        # + 4. Класс Phone в коді оголошено
        # + 5. Класс Phone наслідується від класу Field в коді
        # + 6. Класс Phone зберігає валідний телефон "0504567890" в атрибуті value
        # + 7. Класс Phone не зберігає не валідний телефон "12345abcde" в атрибуті value та викидає виключення ValueError
        # + 8. Класс Phone не зберігає не валідний телефон "050456789" в атрибуті value та викидає виключення ValueError
        # + 9. Класс Phone не зберігає не валідний телефон "05045678901" в атрибуті value та викидає виключення ValueError

    
    def __init__(self, value)-> None:
        if len(value) == 10 and value.isdigit():
            super().__init__ (value)
        else:
            raise ValueError

class Record:

    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів. \\\
    # Відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name

    # Функціональність:
        # Додавання телефонів.
        # Видалення телефонів.
        # Редагування телефонів.
        # Пошук телефону.

    # Критерії приймання
        # Реалізовано зберігання об'єкта Name в окремому атрибуті.
        # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
        # Реалізовано методи для додавання - add_phone/видалення - remove_phone/редагування - edit_phone/пошуку об'єктів Phone - find_phone.

    # + 10. Класс Record в коді оголошено
    # = 11. Класс Record має метод add_phone
    # = 12. Класс Record має метод remove_phone
    # = 13. Класс Record має метод edit_phone
    # = 14. Класс Record має метод find_phone
    # 1. Перевірка виконання методу find_phone класу Record. Успішно знайдено перший номер контакту
    # 2. Перевірка виконання методу find_phone класу Record. Успішно знайдено другий номер контакту
    # 3. Перевірка виконання методу find_phone класу Record для не існуючого номеру. Повернуто значення None
    # 4. Перевірка редагування номера телефону методом edit_phone класу Record успішна
    # 5. Перевірка редагування номера телефону, що не існує, методом edit_phone класу Record успішна. Викинуте виключення ValueError
    # 6. Перевірка видалення номера телефону методом remove_phone класу Record успішна

    # реалізація класу
    
    def __init__(self, name)-> None:
        self.name = name.value
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self):
        ...

    def remove_phone(self):
        ...

    def edit_phone(self):
        ...
    
    def find_phone(self):
        ...



class AddressBook(UserDict):
    # Клас для зберігання та управління записами. Успадковується від UserDict, та містить логіку пошуку за записами до цього класу

    # Функціональність:
        # Додавання записів.
        # Пошук записів за іменем.
        # Видалення записів за іменем.

    # Критерії приймання:
        # Реалізовано метод add_record, який додає запис до self.data.
        # Реалізовано метод find, який знаходить запис за ім'ям.
        # Реалізовано метод delete, який видаляє запис за ім'ям.
        # Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.

        # + 15. Класс AddressBook в коді оголошено
        # + 16. Класс AddressBook наслідується від класу UserDict в коді
        # = 17. Класс AddressBook має метод add_record
        # = 18. Класс AddressBook має метод find
        # = 19. Класс AddressBook має метод delete
        # 1. Перевірка виконання методу add_record класу AddressBook успішна
        # 2. Перевірка виконання методу find класу AddressBook успішна
        # 3. Перевірка виконання методу find класу AddressBook з записом, що не існує успішна
        # 4. Перевірка виконання методу delete класу AddressBook успішна
        # 5. Перевірка виконання методу delete класу AddressBook з записом, що не існує успішна
    
    def add_record(self, user: Record):
        phone_book[user.name] = user.phones

    def find(self, name):
        ...

    def delete(self, name):
        # phone_book.delete(name)
        ...


phone_book = AddressBook()

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


@deco_error
def add_func(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    user = Record(name)
    phone_book.add_record(user)
    
    
    return f"User {name} is added to the phone book with phone number {phone}"


@deco_error
def change_func(*args):
    name = args[0]
    phone = args[1]  
    user = phone_book[name]
    if user: 
        phone_book[name] = phone
        return f"Phone number for user {name} has been changed to {phone}"


@deco_error
def hello_func():
    return "How can I help you?"


def main():

    while True:
        user_input = input(">>>: ")
       
        if user_input.lower() == "exit" or user_input.lower() == "close" or user_input.lower() == "good bye":
            print ("Good bye!")
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
    "Show All": show_func
    }

    user_input = user_input.title()

    for kw, command in COMMANDS.items():
        if user_input.startswith(kw):
            return command, user_input[len(kw):].strip().split()
    return unknown_command, []

@deco_error
def search_func(*args):
    name = Name(args[0])
    user = phone_book[name]
    if user: 
        phone_number = phone_book.get(name)
        return f"The phone number of user {name} is {phone_number}"
    

@deco_error
def show_func():
    return phone_book


def unknown_command():
    return "Unknown command. Try again."

if __name__ == '__main__':
    main()
