with open('subject_list.txt', 'r') as my_file:
    for line in my_file:
        string = line
        cache = '0'
        dict = {}
        max = 0
        list = string.split()
        for el in list:
            if list.index(el) == 0:
                pop = len(el)
                subj = el[:(pop-1)]
            else:
                for sym in el:
                    if sym.isnumeric() is True:
                        cache += sym
            hour = int(cache)
            if hour > 0:
                max += hour
                cache = '0'
        print(f"По предмету {subj} будет проведено {max} занятий")
        cache_dict = {subj: max}
        dict.update(cache_dict)
print(dict)