import time

file_name = "Каша из топора.txt"
substring = input("Введите искомое слово: ")

with open(file_name, 'r', encoding='CP1251') as f: #'r' - функция чтения(.read)
    text = f.read()

start_time = time.time()
count = text.count(substring)
end_time = time.time()

print(f"Файл: {file_name}")
print(f"Слово: '{substring}'")
print(f"Количество слов: {count}")
print(f"Время выполнения встроенного поиска: {end_time - start_time:.6f} секунд")