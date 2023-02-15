#Second variant
import csv

def esc(code):
    return f'\u001b[{code}m'

def flag_bangladesh():
    print(f'{GREEN}{" " * 30}{END}')
    print(f'{GREEN}{" " * 8}{RED}{" " * 6}{GREEN}{" " * 16}{END}')
    print(f'{GREEN}{" " * 6}{RED}{" " * 10}{GREEN}{" " * 14}{END}')
    print(f'{GREEN}{" " * 4}{RED}{" " * 14}{GREEN}{" " * 12}{END}')
    print(f'{GREEN}{" " * 4}{RED}{" " * 14}{GREEN}{" " * 12}{END}')
    print(f'{GREEN}{" " * 6}{RED}{" " * 10}{GREEN}{" " * 14}{END}')
    print(f'{GREEN}{" " * 8}{RED}{" " * 6}{GREEN}{" " * 16}{END}')
    print(f'{GREEN}{" " * 30}{END}')

def uzor_R(n):
    print((f'{BLACK}{"  " * 5}{WHITE}{"  " * 3}{END}') * n)
    print((f'{BLACK}{"  " * 1}{WHITE}{"  " * 3}{BLACK}{"  " * 1}{WHITE}{"  " * 3}{END}') * n)
    print((f'{BLACK}{"  " * 1}{WHITE}{"  " * 1}{BLACK}{"  " * 3}{WHITE}{"  " * 3}{END}') * n)
    print((f'{BLACK}{"  " * 1}{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 5}{END}') * n)
    print((f'{BLACK}{"  " * 1}{WHITE}{"  " * 1}{BLACK}{"  " * 6}{END}') * n)

def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = st * (8 - i) + st
            if i == 9:
                array_in[i][j] = j
    return array_in

def array_fill(array_fi, res, st):
    for i in range(9):
        for j in range(10):
            if abs(array_fi[i][0] - res[9 - j]) < st:
                for k in range(9):
                    if 8 - k == j:
                        array_fi[i][k + 1] = 1
    return array_fi


def draw_plot(array_pl):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + '\t' + str(int(array_pl[i][j])) + '\t'
            if array_pl[i][j] == 0:
                line += '  '
            if array_pl[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '\t0\t1 2 3 4 5 6 7 8 9 ' + END)  

RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
GREEN = esc(42)
BLACK = esc(40)
END = esc(0)

# 1 task
print('First task: ')
flag_bangladesh()
print()

# 2 task
print('second task: ')
n = 9
uzor_R(n)
print()

# 3 task
print('third task: ')

array_plot = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = 2 * i + 3
step = round(abs(result[0] - result[9]) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
draw_plot(array_plot)
print()

# 4 task
with open('books.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    table_list = list(table)

    before_count = 0
    after_count = 0
    for row in table_list[1:]:
        year = int(row[6][:4])
        if (year <= 2015):
            before_count += 1
        else:
            after_count += 1

sum = before_count + after_count
a = before_count * 100 // sum
b = after_count * 100 // sum 

print(f'{"До 2015    "}{BLUE}{"  " * a}{END}{" "}{str(a)}{"%"}')
print()
print(f'{"После 2015 "}{BLUE}{"  " * b}{END}{" "}{str(b)}{"%"}')
print()