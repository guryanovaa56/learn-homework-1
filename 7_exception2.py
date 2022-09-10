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
class AppError(Exception):
    """Application Error."""


class MaxDiscountError(AppError):
    """Maximum Discount over 99"""


def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
    except TypeError:
        raise AppError('Агрументы должны быть числами')
    except ValueError:
        raise AppError('Args must be float')

    if max_discount > 99:

        raise AppError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)


if __name__ == "__main__":
    print(discounted(100, 3,100))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
