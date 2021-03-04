#1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.
duration = int(input("Введите время в секундах:"))

duration_day = duration // 86400
duration_hour = (duration // 3600) % 24
duration_min = (duration // 60) % 60
duration_sec = duration % 60

if duration < 60:
    print(duration, 'сек')
elif duration >= 60 and duration < 3660:
    print(duration_min, 'мин', duration_sec, 'сек')
elif duration >= 3660 and duration < 86400:
    print(duration_hour, 'час', duration_min, 'мин', duration_sec, 'сек')
elif duration >=86400:
    print(duration_day, 'дн', duration_hour, 'час', duration_min, 'мин', duration_sec, 'сек')