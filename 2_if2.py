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
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    
    if str1 == str2:
        return 1
    
    if len(str1) > len(str2) :
        return 2
    
    if str1 != str2 and str2 == 'learn':
        return 3
    
    return None

def main():
    assert check_str('test', 'learn') == 3
    assert check_str(2, 3) == 0
    assert check_str('test', 'test') == 1
    assert check_str('long_test', 'test') == 2
    assert check_str('test', 'long_test') == None
     
    
if __name__ == "__main__":
    main()
