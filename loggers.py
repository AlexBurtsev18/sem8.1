def find_data():
    print('Введите имя файла: ')
    file_name = input()

    data = open(file_name + '.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()


def new_data():
    new_file_name = str(input("Введите название нового файла: "))
    data = open(new_file_name + '.txt', 'w', encoding='utf-8')
    print("Введите ФИО и номер телефона (+7) через пробел: ")
    original_data = input()
    data.write(original_data)
    data.close()

def correct_data():
    file_name = input('Введите имя файла: ')
    with open(file_name + '.txt', 'r', encoding='utf-8') as file:
        for row in file:
            contact = row.split(" ")
            num = input("Для смены фамилии нажми 0, имени - 1, отчества - 2, телефона - 3 ")
            contact[int(num)] = input("Введите новые данные: ")
    with open(file_name + '.txt', 'w', encoding='utf-8') as file:
        file.writelines(" ".join(contact))
    print('Контакт изменен.')
    # choise_num = int(input('Выберите элемент, который хотите заменить\n'
    #     '0 - Фамилия\n'
    #     '1 - Имя\n'
    #     '2 - Отчество\n'
    #     '3 - телефон\n'
    #     '5 - выйти из программы\n'))
    # data = open(file_name + '.txt', 'w', encoding='utf-8')
    # original_data = input("Введите НОВЫЕ ФИО и номер телефона (+7) через пробел: ")
    # data.write(original_data)
    # data.close()
import os
def delete_data():
    name = input('Введите имя файла, который хотите удалить: ')
    print(os.path.abspath(name + '.txt'))
    name = os.path.abspath(name + '.txt')
    os.remove(name)


    