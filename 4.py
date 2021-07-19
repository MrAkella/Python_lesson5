def translator(word):
    if word == 'One':
        word = 'Один'
        return word
    elif word == 'Two':
        word = 'Два'
        return word
    elif word == 'Three':
        word = 'Три'
        return word
    elif word == 'Four':
        word = 'Четыре'
        return word
    else:
        return word

with open("list_of_num.txt") as my_file:
    with open("new_list_of_num.txt", 'a+') as changed_file:
        for line in my_file:
            linechange = line.split()
            for el in linechange:
                if el != translator(el):
                    changed_file.write(translator(el))
                    changed_file.write(' ')
                else:
                    changed_file.write(el)
                    changed_file.write(' ')
            changed_file.write('\n')
with open("new_list_of_num.txt") as result:
    print(result.read())