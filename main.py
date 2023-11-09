# Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска
# определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1.Создать файл для записи телефонной книги
#     1.1 открытие файла на дозапись
# 2. Подготовка меню для пользователя

# 2. Запись данныч в файл по каждому контакту
#     2.1 ввод данных пользователем
#     2.2 подготовка данных для записи в файл
#     2.3 открытие файла в режиме дозаписи
#     2.4 запись новой строки с данными
# 3. Чтене данных из файла
#     3.1 открытие файла в режиме чтения
#     3.2 считать все данные и вывести их на экран.
# 4. Поиск записей по параметрам и вывод соответствующих данных
#     4.1 ввод пользователей параметра поиска
#     4.2
#     4.3 считать все данные из файла

import colorama
from colorama import Fore

colorama.init(autoreset=True)


def input_name():
    return input("Введите имя контакта: ")


def input_surname():
    return input("\nВведите фамилию контакта: ")


def input_patronymic():
    return input("Введите отчество контакта: ")


def input_phone():
    return input("Введите телефон контакта: ")


def input_adress():
    return input("Введите адрес контакта: ")


def read_file():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        return file.read()


def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    str_contact = f"{surname} {name} {patronymic} {phone}\n{adress}\n\n"
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(str_contact)


def print_data():
    print("=======" * 5)
    print(read_file())
    print("=======" * 5)


def search_contact():
    print(Fore.LIGHTMAGENTA_EX + "\nВыберите что искать: \n")
    print("1) Фамилия \n" "2) Имя \n" "3) Отчество \n" "4) Телефон\n" "5) Адрес")
    command = input(Fore.LIGHTGREEN_EX + "Введите номер операции: ")
    while command not in ("1", "2", "3", "4", "5"):
        print(
            Fore.LIGHTRED_EX + "Некорректный ввод номера операции!\n"
            "Повторный ввод от 1 до 5"
        )
        command = input(Fore.LIGHTGREEN_EX + "Введите номер операции: ")
    print()
    i_search_param = int(command) - 1
    search = input(Fore.LIGHTMAGENTA_EX +
                   "Введите данные для поиска: ").title()
    all_contacts = read_file().strip().split("\n\n")
    for contact_str in all_contacts:
        contact_lst = contact_str.replace("\n", " ").split()
        if search in contact_lst[i_search_param]:
            print(contact_str + "\n")
            return contact_str


def change_contact():
    print(
        Fore.LIGHTMAGENTA_EX_EX
        + "Введите параметры контакта, в котором хотите внести изменения"
    )
    contact_string = search_contact()
    contact_list = contact_string.replace("\n", " ").split()
    print(Fore.LIGHTGYELLOW_ex + "Выберите, что будем изменять в контакте: ")
    print(
        "1) Фамилия \n"
        "2) Имя \n"
        "3) Отчество \n"
        "4) Телефон\n"
        "5) Адрес \n"
        "6) Удалить контакт"
    )
    command = input(Fore.LIGHTGREEN_EX + "Введите номер операции: ")
    while command not in ("1", "2", "3", "4", "5", "6"):
        print(
            Fore.LIGHTRED_EX + "Некорректный ввод номера операции!\n"
            "Повторный ввод от 1 до 6\n"
        )
        command = input(Fore.LIGHTGREEN_EX + "Введите номер операции: ")
        print()
    i_change_param = int(command) - 1
    if command == "6":
        contact_list.clear()

        new_file = read_file().strip().replace(contact_string, "")
        print(new_file)
        with open("phonebook.txt", "w", encoding="UTF-8") as file:
            file.write(new_file)
        return

    else:
        new_param = input(Fore.LIGHTRED_EX + "Введите новый параметр: ")
        contact_list[i_change_param] = new_param
        contact_str = f"{contact_list[0]} {contact_list[1]} {contact_list[2]} {contact_list[3]}\n{contact_list[4]}\n\n "

    new_file = read_file().strip().replace(contact_string, contact_str)
    print(new_file)
    with open("phonebook.txt", "w", encoding="UTF-8") as file:
        file.write(new_file)
        return


def interface():
    with open("phonebook.txt", "a", encoding="utf-8"):
        pass

    command = ""
    while command != "5":
        print(Fore.LIGHTYELLOW_EX +
              "\nВыберите вариант работы с телефонной книгой: \n")
        print(
            "1) Запись данных \n"
            "2) Вывод телефонной книги на экран \n"
            "3) Поиск данных \n"
            "4) Изменение данных\n"
            "5) Выход"
        )
        command = input(Fore.LIGHTGREEN_EX + "Введите номер операции: ")
        while command not in ("1", "2", "3", "4", "5"):
            print(
                Fore.LIGHTRED_EX + "Некорректный ввод номера операции!\n"
                "Повторный ввод"
            )
            command = input(Fore.LIGHTGREEN_EX + "Введите номер операции: ")
            print()

        match command:
            case "1":
                input_data()
            case "2":
                print_data()
            case "3":
                search_contact()
            case "4":
                change_contact()
            case "5":
                print(Fore.LIGHTBLUE_EX + "Всего хорошего, до встречи")


interface()
