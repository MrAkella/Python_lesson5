with open("number_set.txt", 'w') as my_file:
    my_file.write('0 1 2 3 4 5 6 7 8 9')  # НЕПРАВИЛЬНО
my_file = open('number_set.txt')
my_file_list = my_file.read()
sum = 0
for el in my_file_list:
    if el.isnumeric() is True:
        sum = sum + int(el)
print(f"Сумма чисел составляет {sum}")
my_file.close()


# РАНДОМНАЯ ГЕНЕРАЦИЯ!!!