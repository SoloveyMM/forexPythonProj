import datetime
from forex_python.converter import CurrencyRates, convert

def number_check(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def vvod_date():
    print('Введите дату в формате DD.MM.YYYY: ')
    date = input().split('.')
    y = int(date[2])
    m = int(date[1])
    d = int(date[0])
    return y, m, d

def vFile(iz, v, sk, year, month, day):
    c = CurrencyRates()
    file = open('hist.txt', 'a')
    file.write('Конвертировал ' + str(sk) + ' ' + str(iz) + ' в ' + str(v) +
               ' по курсу ' + str(round(c.get_rate(iz, v, date_obj=datetime.date(year, month, day)), 4)) +
               ' и получил ' + str(round(c.convert(iz, v, sk, date_obj=datetime.date(year, month, day)), 4)) + '\n')
    file.close()


def letter_check(letter):
    c = CurrencyRates()
    if letter in c.get_rates('USD'):
        return True
    else:
        return False



def get_history():
    f = open('hist.txt', 'r')
    lines = f.read().splitlines()
    for i in range(len(lines)):
        print(lines[i])
    f.close()



if __name__ == '__main__':
    file = open('hist.txt', 'w')
    file.close()
    exit = 'yes'
    while exit != 'no' and exit != 'NO':
        iz = input('Введите валюту, из которой перевести: ')
        while letter_check(iz) != True:
            iz = input('Ошибка! Повторите ввод: ')
        v = input('Введите валюту, в которую надо перевести: ')
        while letter_check(v) != True:
            v = input('Ошибка! Повторите ввод: ')
        sk = input('Введите количество: ')
        while number_check(sk) != True:
            sk = input('Ошибка! Повторите ввод: ')
        sk = float(sk)
        date = input('Желаете ввести дату? (yes/no): ')
        while date != 'yes' and date != 'YES' and date != 'no' and date != 'NO':
            date = input('Ошибка! Повторите ввод: ')
        if date == 'yes' or date == 'YES':
             data = vvod_date()
             vFile(iz, v, sk, data[0], data[1], data[2])
        else:
             vFile(iz, v, sk, datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day)
        history = input('Вывести историю? (yes/no): ')
        while history != 'yes' and history != 'YES' and history != 'no' and history != 'NO':
            history = input('Ошибка! Повторите ввод: ')
        if history == 'yes' or history == 'YES':
            get_history()
        exit = input('Продолжить? (yes/no): ')
        while exit != 'yes' and exit != 'YES' and exit != 'no' and exit != 'NO':
            exit = input('Ошибка! Повторите ввод: ')


