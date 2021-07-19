my_file = open('test_text.txt')
linecount = 0
words = 0
for line in my_file:
    linecount += 1
    linesize = line.split()
    word = len(linesize)
    print(f"В {linecount} строке записано {word} слов")
    words += word
print(f"В данном текстовом документе всего {linecount} строк и {words} слов")
my_file.close()