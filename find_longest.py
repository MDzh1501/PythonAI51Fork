input_filename = "D:\\IT school\\Projects\\Git_learning\\Git_word\\PythonAI51PublicHForc\\input.txt"
words = []

try:
    with open(input_filename, 'r', encoding='utf-8') as file:
        for line in file:
            words.append(line.strip())
    print('Прочитані слова:', words)
except FileNotFoundError:
    print(f'Помилка: Файл "{input_filename}" не знайдено.')