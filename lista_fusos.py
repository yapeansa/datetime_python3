#!/bin/python3

import pytz

# Lista de Fusos horários

print('Lista de fusos horários:')

for tz in pytz.all_timezones:
    print(tz)
