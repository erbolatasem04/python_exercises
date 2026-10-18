'''
Перевод температуры. Цельсий -> Фаренгейт: F = C * 9/5 + 32.
'''

temp_str = input('write temp:')

try:
    temp = int(temp_str)
    F = temp * 9/5 + 32
    print(f'{temp} change on farangeit wiil be {F}')
except ValueError:
    print("write int!")

