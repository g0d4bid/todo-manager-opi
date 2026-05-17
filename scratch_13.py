import time

def linear_search(text, pattern):
    count = 0
    n = len(text)
    m = len(pattern) #слово

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]: #неравенство
                match = False
                break
        if match:
            count += 1
    return count

file_name = "Каша из топора.txt"
substring = input("Введите искомое слово: ")

with open(file_name, 'r', encoding='CP1251') as f: #'r' - функция чтения(read) и CP1251 - для декодировки под винду
    text = f.read()

start_time = time.time()
count = linear_search(text, substring)
end_time = time.time()

print(f"Файл: {file_name}")
print(f"Слово: '{substring}'")
print(f"Количество слов: {count}")
print(f"Время выполнения линейного поиска: {end_time - start_time:.6f} секунд")