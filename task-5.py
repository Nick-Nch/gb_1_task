gain = int(input('Введите выручку: '))
cost = int(input('Введите издержку: '))
difference = gain - cost
if (gain > cost):
    print('Ваша вуручка=' + str(difference))
elif (gain < cost):
    print('Ваш убыток=' + str(abs(difference)))
elif (gain == cost):
    print('Работа в 0')

if (gain > cost):
    people = int(input('Введите количество сотрудников: '))
    print('Выручка на человека: ' + str(difference / people))

