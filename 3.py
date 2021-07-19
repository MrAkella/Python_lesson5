my_file = open('namelist.txt', 'r', encoding='utf-8')
listing = []
max = 0
count = 0
name = 'name'
for line in my_file:
    count += 1
    lineread = line.split()
    for el in lineread:
        if el.isnumeric() is False:
            name = el
        if el.isnumeric() is True:
            if int(el) < 20000:
                listing.append(name)
                listing.append(' ')
            max += int(el)
print(f"Оклад менее 20 тыс. имеют: {''.join(listing)}")
print(f"Средняя заработная плата составляет {max//count}")
my_file.close()