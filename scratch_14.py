import time

def kmp_search(text, pattern):
    def compute_prefix(pattern): #(префикс функция) каждый элемент показывает длину наибольшего собственного суффикса, который является префиксом
        m = len(pattern) #слово
        prefix = [0] * m #повторяет список [0] m количество раз
        k = 0
        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = prefix[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            prefix[q] = k
        return prefix

    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    count = 0
    prefix = compute_prefix(pattern)
    q = 0  #количество совпавших символов

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = prefix[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            count += 1
            q = prefix[q - 1]
    return count

file_name = "Каша из топора.txt"
substring = input("Введите искомое слово: ")

with open(file_name, 'r', encoding='CP1251') as f:
    text = f.read()

start_time = time.time()
count = kmp_search(text, substring)
end_time = time.time()

print(f"Файл: {file_name}")
print(f"Слово: '{substring}'")
print(f"Количество слов: {count}")
print(f"Время выполнения алгоритма КМП: {end_time - start_time:.6f} секунд")