'''
Стоимость покупки. Вводятся цена и количество. Цена × количество, если сумма > 1000 -> скидка 10%.
'''

price_str = input('print price of 1 apple:')

try:
    price = int(price_str)
    count_str = input('print count of apple:')
    try:
        count = int(count_str)
        total = price * count
        if total > 1000:
            discount = total * 0.9
            print(f'you have discount 10%,with discount total price is {discount}')
        else:
            print(f' total price is {total}')
    except ValueError:
        print('write int count!')
except ValueError:
    print('write int price!')

