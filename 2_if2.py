"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def check_str(str1, str2):
    if type(str1) is not str or type(str2) is not str:
        return '0'
    elif str1 == str2:
        return '1'
    elif len(str1) > len(str2) :
        return '2'
    elif str1 != str2 and str2 == 'learn':
        return '3'


def main():
    str1 = 'test'
    # str2 = 'test_test'
    # str2 = "2"
    #str2 = 2
    str2 = 'learn'
    
    print(check_str(str1, str2))


    
if __name__ == "__main__":
    main()
