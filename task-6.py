first_day = int(input('Введите результат бега за первый день: '))
last_day = int(input('Введите конечный результат км: '))
# day = (first_day / 100) * 110
result = 1
km = first_day

while km < last_day:
    km = km + (0.1 * km)
    result += 1
    km = km + first_day
print(f'Вы получите необходимые показатели на %.d день' % result )

