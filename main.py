# tele01 = ['Иванов', 'Василий', 'Петрович', '+79990000001']
# tele01 = ', '.join(tele01)
# data = open('data01.txt', 'w', encoding= 'utf-8')
# data.writelines(tele01)
# data.close()

# tele02 = ['Петров', 'Геннадий', 'Семенович', '+79991110011']
# tele02 = ', '.join(tele02)
# data = open('data02.txt', 'w', encoding= 'utf-8')
# data.writelines(tele02)
# data.close()

# tele03 = ['Петрова', 'Галина', 'Семеновна', '+79091110022']
# tele03 = ', '.join(tele03)
# data = open('data03.txt', 'w', encoding= 'utf-8')
# data.writelines(tele03)
# data.close()

from loggers import find_data, new_data, correct_data, delete_data
import os

def interface():
    print("Здравствуй пользователь!")
    print('Вы находитесь в меню справочника')
    print('1 - найти запись\n'
        '2 - новая запись\n'
        '3 - редактирование записи\n'
        '5 - удаление записи\n'
        '0 - выйти из программы\n')

    while True:
        command = int(input("Введите номер команды(1-0): "))
        if command not in [1,2,3,4,5,0]:
            print("Ошибочный запрос!")
        elif command == 1:
            find_data()
        elif command == 2:
            new_data()
        elif command == 3:
            correct_data()
        elif command == 5:
            delete_data()
        elif command == 0:
            print('Всего доброго!')
            return
        
if __name__ == "__main__":
    interface()