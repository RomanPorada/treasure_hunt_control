import random  
  
# Створення карти за заданими розмірами  
def create_board(rows, cols):  
    board = []  
    for i in range(rows):  
        row = []  
        for j in range(cols):  
            row.append(' ')  
        board.append(row)  
    return board  
  
# Розмір карти за складністю  
level_sizes = {'легкий': 5, 'середній': 10, 'складний': 20}  
  
# Запит ім'я користувача  
while True:  
    name = input("Введіть свій псевдонім: ")  
    if name.strip() != "":  
        break  
  
# Запит складності  
while True:  
    level = input("Виберіть рівень складності (легкий, середній, складний): ")  
    if level in level_sizes:  
        rows = cols = level_sizes[level]  
        break  
  
# Генерація координат скарбу  
treasure_row = random.randint(0, rows-1)  
treasure_col = random.randint(0, rows-1) 

# генерація координат першої води
wether_row_1 = random.randint(0, rows-1)
wether_col_1 = random.randint(0, rows-1)

# генерація координат другої води
wether_row_2 = random.randint(0, rows-1)
wether_col_2 = random.randint(0, rows-1)
  
# Початок гри  
board = create_board(rows, cols)  
board[treasure_row][treasure_col]  
  
print("Карта сформована! Успішного пошуку скарбів♥")
for i in range(rows):  
    print(" " + "___" * cols)  
    row_str = "|"  
    for j in range(cols):  
        row_str += " {} |".format(board[i][j])  
    print(row_str)  
print(" " + "___" * cols)  
  
print("Гра почалася, {}! Ваше завдання - знайти скарб, розташований на карті. Успіхів та перемоги!".format(name))



abb = (treasure_row, treasure_col)
wether_1 = (wether_row_1, wether_col_1)
wether_2 = (wether_row_2, wether_col_2)
attemps = 5

while True:
    plaing = input('Ведіть номер рядка: ')
    plaing2 = input(f'Ведіть номерацію клітинки {plaing}-го рядка: ')
    plaing_result = ('('+ plaing + ', ' + plaing2 +')')

    print(plaing_result)

    if plaing_result == str(abb):
        print('Вітаю, ви знайшли скарб! ')
        break
    elif plaing_result == str(wether_1) or plaing_result == str(wether_2):
        print("вітаю ви знайшли воду кількість ходів збільшилася на 2")
        attemps += 2
    else:
        print('Нажаль тут пусто :( ')
        attemps -=1
    
    if attemps > 0:
        print('Спробуйте ще раз, у вас залишилось '+str(attemps)+' спроб!')

    else:
        print('Нажаль ви програли, скарб був розташований на кординатах '+str(abb))
        break