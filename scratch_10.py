a = 'Съешь ещё этих мягких французских булок, да выпей чаю'
b = ' '
print(f'Строка: {a}')
counter_a = 1
for item in a:
    if item in b:
        counter_a += 1
print(f'Количество слов: {counter_a}')