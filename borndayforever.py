"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def is_year(year, minimum=1000, maximum=2999):
    return (year.isdigit() and len(year) >= len(f'{minimum}') and len(year) <= len(f'{maximum}') and
            int(year) >= minimum and int(year) <= maximum)


def find_splitter(input_string):
    splitter_mask = int(' ' in input_string) + (int('.' in input_string) << 1) + \
                    (int('/' in input_string) << 2)
    splitter_sign = ''
    if splitter_mask == 1:
        splitter_sign = ' '
    elif splitter_mask == 2:
        splitter_sign = '.'
    elif splitter_mask == 4:
        splitter_sign = '/'
    return splitter_sign


def ddmm_check(datestring):
    splitter_sign = find_splitter(datestring)
    correct = False
    day = month = 0
    if datestring!= '' and splitter_sign != '':
        splitted_string = datestring.split(splitter_sign)
        if len(splitted_string) == 2:
            if (splitted_string[0].isdigit() and int(splitted_string[0]) >= 1 and
                    int(splitted_string[0]) <= 31 and splitted_string[1].isalpha()):
                day = int(splitted_string[0])
                month_names = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6, 'июля': 7,
                               'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
                month = month_names[(splitted_string[1].lower())]
                correct = True
            elif splitted_string[0].isdigit() and splitted_string[1].isdigit():
                if (splitter_sign == '.' and int ( splitted_string[0]) >= 1 and
                        int(splitted_string[0]) <= 31 and int(splitted_string[1]) >= 1 and
                        int(splitted_string[0]) <= 12):
                    day = int(splitted_string[0])
                    month = int(splitted_string[1])
                    correct = True
                elif (splitter_sign == '/' and int(splitted_string[0]) >= 1 and
                      int(splitted_string[0]) <= 12 and int(splitted_string[1]) >= 1 and
                      int(splitted_string[0]) <= 31):
                    day = int(splitted_string[1])
                    month = int(splitted_string[0])
                    correct = True
            month_length = {0: 0, 1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            if day > month_length[month]:
                correct = False
    if correct:
        return [month, day]
    else:
        return [0, 0]


ans_yr = ''
while not is_year(ans_yr) or int(ans_yr) != 1799:
    ans_yr = input('Укажите год рождения А.С. Пушкина: ')

ans_dm = ''
while ddmm_check(ans_dm) != [6, 6]:
    ans_dm = input('Укажите дату рождения А.С. Пушкина: ')
    if ddmm_check(ans_dm) == [5, 26]:
        print('Вы указали день рождения по юлианскому календарю, но это тоже...')
        break

print('Верно')
