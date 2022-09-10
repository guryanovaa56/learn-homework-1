"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
stock =[
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

def amount_sold():
  amount= []
  for phone in stock:
      phone_dict = {
            'product': phone['product'],
            'amount_sold': sum(phone['items_sold']),
            'quantity_sold': len(phone['items_sold'])}
      amount.append(phone_dict) 
  return amount

def total_sold():
  total_amount = 0
  total_qnt = 0
  for phone in stock:
    total_amount += sum(phone['items_sold'])
    total_qnt += len(phone['items_sold'])
  all_stock = {'total amount' : total_amount,
  'total_qnt' : total_qnt}
  return all_stock

def main():
 res_phone = amount_sold()
 all_stock = total_sold()
 avg_sold = all_stock['total amount'] // all_stock['total_qnt']
 
 for phone in res_phone:
        print(f'Суммарное количество продаж {phone["product"]}: {phone["amount_sold"]}')
        print(f'Среднее количество продаж {phone["product"]}:')
        print(f' {phone["amount_sold"] // phone["quantity_sold"]}')
 
 
 print(f'Суммарное количество продаж всех товаров: {all_stock["total amount"]}')
 print(f'Среднее количество продаж всех товаров: {avg_sold}')
 
 
      

    
if __name__ == "__main__":
    main()
