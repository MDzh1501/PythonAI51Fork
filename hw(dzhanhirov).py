def find_the_longest(name):
    with open(name, 'r', encoding='utf-8') as f:
        return max((line.strip('\n') for line in f), key=len)

print(find_the_longest('files/input.txt'))
