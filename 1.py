import datetime
import time


def decor(old_fuction):
    def new_function(*args, **kwars):
        result = old_fuction(*args, **kwars)

        with open('test.txt', "a+", encoding="utf-8") as result_file:
            result_file.write(f'Дата и время: {datetime.datetime.now()}' + '\n')
            result_file.write(f'Функция: {old_fuction.__name__}' + '\n')
            result_file.write(f'Аргументы: {args} {kwars}' + '\n')
            result_file.write(f'Возвращаемый результат: {result}' + '\n')
            result_file.write('\n')

        return result

    return new_function



@decor
def my_function(a, b):
    return a + b


my_function(7, 4)
time.sleep(2)
my_function(6, 6)
