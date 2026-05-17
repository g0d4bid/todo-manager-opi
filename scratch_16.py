import time

def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0 or n < m:
        return 0

    prime = 101 #число для хэширования
    base = 256

    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    count = 0

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                count += 1

        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime

            if text_hash < 0:
                text_hash += prime

    return count

file_name = "Каша из топора.txt"
substring = input("Введите искомое слово: ")

with open(file_name, 'r', encoding='CP1251') as f:
    text = f.read()

start_time = time.time()
count = rabin_karp_search(text, substring)
end_time = time.time()

print(f"Файл: {file_name}")
print(f"Слово: '{substring}'")
print(f"Количество слов: {count}")
print(f"Время выполнения алгоритма Рабина-Карпа: {end_time - start_time:.6f} секунд")