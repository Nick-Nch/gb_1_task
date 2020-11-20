


while True :
    user_sec = int(input('Введите секунды и stop для остановки: '))
    h = user_sec // 3600
    m = (user_sec - h * 3600) // 60
    s = user_sec - (h * 3600 + m * 60)
    print(f'Время:  {h}:{m}:{s}')
    if user_sec == 'stop':
        break



