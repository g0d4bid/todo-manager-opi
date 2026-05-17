a = 'цукщкышыпвшероввшщпровпшщзол'
b = 'аоуеяыю'
print(f'Строка символов: {a}')
counter_a = 0
for item in a:
    if item in b:
        counter_a += 1
print(f'Количество гласных: {counter_a} ')