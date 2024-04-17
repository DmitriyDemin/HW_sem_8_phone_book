# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
import os

def read_data(file_name):
    os.system('cls')
    phone_book = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            entry = line.strip().split(';')
            phone_book.append({'last_name': entry[0], 'first_name': entry[1], 'middle_name': entry[2], 'phone_number': entry[3]})
        print("Телефонный справочник прочитан, готов к работе.")
    return phone_book


def save_data(file_name, phone_book):
    with open(file_name, 'w', encoding='utf-8') as file:
        for entry in phone_book:
            file.write(';'.join([entry['last_name'], entry['first_name'], entry['middle_name'], entry['phone_number']]) + '\n')
    print(f"Контакт сохранен.")


def open_data(phone_book, search=False):
    if phone_book:
        print("{:<5} {:<15} {:<15} {:<15} {:<15}".format("№", "Фамилия", "Имя", "Отчество", "Телефон"))
        print("-" * 4 + "+" + "-" * 14 + "+" + "-" * 14 + "+" + "-" * 14 + "+" + "-" * 14)
        for idx, entry in enumerate(phone_book, start=1):
            print("{:<5} {:<15} {:<15} {:<15} {:<15}".format(idx, entry['last_name'], entry['first_name'], entry['middle_name'], entry['phone_number']))
    

def export_data(phone_book):
    print("Оставьте пустым для экспорта всего справочника")
    print("Для возврата в главное меню введите 0")
    index = input("Введите номер записи для экспорта: ")
    if index:
        index = int(index) - 1
        if 0 <= index - 1 < len(phone_book):
            entry = phone_book[index]
            file_path = input("Введите имя файла для экспорта (без расширенрия): ") + ".txt"
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("{},{},{},{}".format(entry['last_name'], entry['first_name'], entry['middle_name'], entry['phone_number']))
            print("Запись успешно экспортирована в файл {}.".format(file_path))
        elif int(index) == -1:
            print("Эксопрт отменен.")
        else:
            print("Нет такой записи.")
    else:
        print("Экспорт всего справочника...")
        file_path = input("Введите имя файла для экспорта (без расширения): ") + ".txt"
        with open(file_path, 'w', encoding='utf-8') as file:
            for entry in phone_book:
                file.write("{},{},{},{}\n".format(entry['last_name'], entry['first_name'], entry['middle_name'], entry['phone_number']))
            print("Справочник успешно экспортирован в файл {}.".format(file_path))

def add_record(phone_book: list, file_name):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    phone_book.append({'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number})
    save_data(file_name, phone_book)

def search_data(phone_book, key, value):
    results = []
    for entry in phone_book:
        if entry[f'{key}'].lower() == value.lower():
            results.append(entry)
    return results

def search_by_value(phone_book):
    while True:
        print (f"Меню поиск:\n1 Поиск по фамилии\n2 Поиск по имени\n3 Поиск по телефону\n0 Вернутся в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            value = input("Введите фамилию для поиска: ")
            results = search_data(phone_book, 'last_name', value)
            open_data(results, True)
        elif choice == '2':
            value = input("Введите имя для поиска: ")
            results = search_data(phone_book, 'first_name', value)
            open_data(results, True)
        elif choice == '3':
            value = input("Введите телефон для поиска: ")
            results = search_data(phone_book, 'phone_number', value)
            open_data(results, True)
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def main():
    file_name = "phone_book.txt"
    phone_book = read_data(file_name)
    while True:
        print (f"Главное меню:\n1 Показать все контакты\n2 Добавить контакт\n3 Поиск контакта\n4 Поделиться контактом\n0 Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            open_data(phone_book)
        elif choice == '2':
            add_record(phone_book, file_name)
        elif choice == '3':
            search_by_value(phone_book)
        elif choice == '4':
            export_data(phone_book)
        elif choice == '0':
            break
        else:
            print("ОШИБКА выбора. Попробуйте снова.")

main()


