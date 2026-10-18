'''
Калькулятор возраста. Запроси год рождения расчитай возраст в 2026 (f-строка).
'''

year_str = input("print year of birth:")
try:
    year = int(year_str)
    age_in_2026 = 2026 - year
    print(f"Age in 2026: {age_in_2026}")
except ValueError as e:
    print('print int!')
