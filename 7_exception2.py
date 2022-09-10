"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    try:
        if(not type(price) is int or not type(discount) is int or not type(max_discount) is int):
            raise TypeError('Агрументы должны быть числами')
        else:
            price = abs(float(price))
            discount = abs(float(discount))
            max_discount = abs(float(max_discount))
            if max_discount > 99:
                raise ValueError('Слишком большая максимальная скидка')
            if discount >= max_discount:
                return price
            else:
                return price - (price * discount / 100)
    except TypeError as not_int:
        print(not_int)
    except ValueError as big_discount:
        print(big_discount)
    
if __name__ == "__main__":
    print(discounted(100, 3,100))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
