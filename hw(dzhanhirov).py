def find_the_longest(name):
    try:
        with open(name, 'r', encoding='utf-8') as f:
            return max((line.strip('\n') for line in f), key=len)
    except FileNotFoundError:
        print(f"Error! File {name} was not found!")

print(find_the_longest('files/input.txt'))
