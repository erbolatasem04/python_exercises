'''
Анкета. Запроси имя, возраст, город -> выведи все данные одной f-строкой.
'''

name = input('write name:')
city = input('write city:')
age_str = input('write age:')
try:
    age = int(age_str)
    print(f'form are: '
          f'name:  {name}, '
          f'age: {age} ,'
          f'city:  {city} ')
except ValueError:
    print('write int age')
