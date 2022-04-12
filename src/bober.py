spisok = []

while True:
    buf = input('Марк говорит введите значение: ')
    if buf == '':
        break
    else:
        spisok.append(buf)

index = 0

while index < len(spisok):
    print(f"МАРК ГОВОРИТ:'. {spisok[index]}")
    index = index + 1