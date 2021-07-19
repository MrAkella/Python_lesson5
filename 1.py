my_file = open('new.txt', 'a+')
while True:
    cache = input('Введите данные: ')
    my_file.write(cache)
    my_file.write("\n")
    if cache == "":
        break
my_file.seek(0)
print(my_file.read())
my_file.close()