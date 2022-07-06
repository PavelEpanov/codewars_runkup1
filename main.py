def find_outlier(integers):
    count = 0
    if integers[0] % 2 == 0:
        count += 1
    if integers[1] % 2 == 0:
        count += 1
    if integers[2] % 2 == 0:
        count += 1

    print(count)

    if count >= 2: # Если список четный, то обрабатываем
        for char in integers:
            if char % 2 == 1:
                return char # Возвращаем нечётное число из четного списка
    else: # Иначе обрабатываем нечетный список
        for char in integers:
            if char % 2 == 0:
                return char  # Возвращаем четное число из нечетного списка

a = find_outlier([1,2, 4, 6, 8])
print(a)

