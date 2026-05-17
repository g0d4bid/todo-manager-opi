a,b = int(input()),int(input())
s = 0
while True:
    if a==b:
        print(f'Прокаток:{s}')
        break
    a/=2
    s+=1
