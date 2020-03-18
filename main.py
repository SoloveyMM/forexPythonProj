from forex_python.converter import convert, get_rates, get_rate
import datetime


# функция вывода истории
def get_history():
    file = open('history.txt', 'r')
    data = file.read().splitlines()
    for i in range(len(data)):
        print(data[i])
    file.close()


# проверка на число
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# проверка аббревиатуру
def check_abb(abb):
    if abb not in get_rates('USD'):
        return False
    else:
        return True


# запись в файл
def write_to_file(val_from, val_to, amount, year=datetime.datetime.today().year, month=datetime.datetime.today().month,
                  day=datetime.datetime.today().day):
    file = open('history.txt', 'a')
    file.write('Конвертировал ' + str(amount) + ' ' + str(val_from) + ' в ' + str(val_to) +
               ' по курсу ' + str(round(get_rate(val_from, val_to, date_obj=datetime.date(year, month, day)), 3)) +
               ' и получил ' + str(
        round(convert(val_from, val_to, amount, date_obj=datetime.date(year, month, day)), 3)) + '\n')
    file.close()


# конвертирование валюты
def convert_money(val_from, val_to, amount):
    ans = input('Желаете ввести дату?\n1 - Да\n2 - Нет\n')
    while ans != '1' or ans != '2':
        if ans == '1':
            date = input('Введите дату в формате DD.MM.YYYY: ').split('.')
            write_to_file(val_from, val_to, amount, int(date[2]), int(date[1]), int(date[0]))
            return round(convert(val_from, val_to, amount, date_obj=datetime.date(int(date[2]), int(date[1]), int(date[0]))), 3)
        elif ans == '2':
            write_to_file(val_from, val_to, amount)
            return round(convert(val_from, val_to, amount), 3)
        else:
            ans = input('Ошибка ввода, попробуйте еще: ')


if __name__ == '__main__':
    file = open('history.txt', 'w')
    file.close()
    ans = None
    while ans != '3':
        print('1 - Конвертировать валюту\n2 - Вывести историю\n3 - Выход')
        ans = input('Выберите вариант ответа: ')
        if ans == '1':
            val_from = input('Введите какую валюту перевести: ')
            while not check_abb(val_from):
                val_from = input('Ошибка ввода, повторите попытку: ')
            val_to = input('Введите в какую валюту перевести: ')
            while not check_abb(val_to):
                val_to = input('Ошибка ввода, повторите попытку: ')
            amount = input('Сколько денег поменять: ')
            while not isfloat(amount):
                amount = input('Ошибка ввода, повторите попытку: ')
            rez = convert_money(val_from, val_to, float(amount))
            print('Вы получили', rez, val_to,'\n')
        elif ans == '2':
            get_history()
        elif ans != '3':
            print('\nОшибка ввода, повторите еще...')
