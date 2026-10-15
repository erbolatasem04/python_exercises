'''
Длинное имя? Если len(name) > 5 → «длинное», иначе «короткое». Имя вводится с консоли
'''

name = input('write name:')

if len(name) > 5:
    print("Dlinnoe")
else:
    print('korotkoe')