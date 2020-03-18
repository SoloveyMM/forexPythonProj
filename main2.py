import datetime
from forex_python.converter import CurrencyRates, convert

def check_val(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_date():
    print('Введите дату в формате DD/MM/YYYY: ')
    date = input().split('/')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    return year, month, day

def into_file(convert_from, convert_to, kol, year, month, day):
    c = CurrencyRates()
    file = open('operations_history.txt', 'a')
    file.write('Конвертировал ' + str(kol) + ' ' + str(convert_from) + ' в ' + str(convert_to) +
               ' по курсу ' + str(round(c.get_rate(convert_from, convert_to, date_obj=datetime.date(year, month, day)), 2)) +
               ' и получил ' + str(round(c.convert(convert_from, convert_to, kol, date_obj=datetime.date(year, month, day)), 2)) + '\n')
    file.close()


def test_sym(abb):
    c = CurrencyRates()
    if abb in c.get_rates('USD'):
        return True
    else:
        return False


def perevod(convert_from, convert_to, kol):
    print('Вводить дату? (Y/N): ')
    vvod = input()
    while vvod != 'Y' or vvod != 'N' or vvod != 'y' or vvod != 'n':
        if vvod == 'y' or vvod == 'Y':
            date = get_date()
            into_file(convert_from, convert_to, kol, date[2], date[1], date[0])
            return round(convert(convert_from, convert_to, kol, date_obj=datetime.date(date[2], date[1], date[0])), 2)
        elif vvod == 'n' or vvod == 'N':
            print('Дата установлена текущая')
            into_file(convert_from, convert_to, kol, datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day)
            return round(convert(convert_from, convert_to, kol), 2)
        else:
            print('Ошибка ввода, попробуйте еще: ')
            vvod = input()

def get_history():
    f = open('operations_history.txt', 'r')
    lines = f.read().splitlines()
    for j in range(len(lines)):
        print(lines[j])
    f.close()

def input_data():
    vvod = 'net'
    while vvod != '2':
        print('0: Работа с валютой\n1: Показать историю\n2: Выйти')
        print('Введите номер от 0 до 2: ')
        vvod = input()
        if vvod == '1':
            get_history()
        elif vvod == '0':
            print('Из какой конвертировать: ')
            convert_from = input()
            while test_sym(convert_from) != True:
                print('Некорректный ввод, попробуйте снова: ')
                convert_from = input()
            print('В какую валюту конвертировать: ')
            convert_to = input()
            while test_sym(convert_to) != True:
                print('Некорректный ввод, попробуйте снова: ')
                convert_to = input()
            print('Количество: ')
            kol = input()
            while check_val(kol) != True:
                print('Некорректный ввод, попробуйте снова: ')
                kol = input()
            kol = float(kol)
            money = perevod(convert_from, convert_to, kol)
            print('Получено', money, convert_to, '\n')
        elif vvod != '2':
            print('\nНекорректный ввод, попробуйте снова: ')

if __name__ == '__main__':
    file = open('operations_history.txt', 'w')
    file.close()
    input_data()
