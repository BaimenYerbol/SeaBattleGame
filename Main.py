import random
#   Настройки

a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
c1, c2, c3, c4, c5, c6, d1, d2, d3, d4, d5, d6 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
e1, e2, e3, e4, e5, e6, f1, f2, f3, f4, f5, f6 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '

A1, A2, A3, A4, A5, A6, B1, B2, B3, B4, B5, B6 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
C1, C2, C3, C4, C5, C6, D1, D2, D3, D4, D5, D6 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
E1, E2, E3, E4, E5, E6, F1, F2, F3, F4, F5, F6 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '

def change_the_squares_for_player(part, element):
    global a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, c5, c6, d1, d2, d3, d4, d5, d6, e1, e2, e3, e4, e5, e6, f1, f2, f3, f4, f5, f6
    if part[0] == 1:
        if part[1] == 1:
            a1 = element
        elif part[1] == 2:
            a2 = element
        elif part[1] == 3:
            a3 = element
        elif part[1] == 4:
            a4 = element
        elif part[1] == 5:
            a5 = element
        elif part[1] == 6:
            a6 = element
    elif part[0] == 2:
        if part[1] == 1:
            b1 = element
        elif part[1] == 2:
            b2 = element
        elif part[1] == 3:
            b3 = element
        elif part[1] == 4:
            b4 = element
        elif part[1] == 5:
            b5 = element
        elif part[1] == 6:
            b6 = element
    elif part[0] == 3:
        if part[1] == 1:
            c1 = element
        elif part[1] == 2:
            c2 = element
        elif part[1] == 3:
            c3 = element
        elif part[1] == 4:
            c4 = element
        elif part[1] == 5:
            c5 = element
        elif part[1] == 6:
            c6 = element
    elif part[0] == 4:
        if part[1] == 1:
            d1 = element
        elif part[1] == 2:
            d2 = element
        elif part[1] == 3:
            d3 = element
        elif part[1] == 4:
            d4 = element
        elif part[1] == 5:
            d5 = element
        elif part[1] == 6:
            d6 = element
    elif part[0] == 5:
        if part[1] == 1:
            e1 = element
        elif part[1] == 2:
            e2 = element
        elif part[1] == 3:
            e3 = element
        elif part[1] == 4:
            e4 = element
        elif part[1] == 5:
            e5 = element
        elif part[1] == 6:
            e6 = element
    elif part[0] == 6:
        if part[1] == 1:
            f1 = element
        elif part[1] == 2:
            f2 = element
        elif part[1] == 3:
            f3 = element
        elif part[1] == 4:
            f4 = element
        elif part[1] == 5:
            f5 = element
        elif part[1] == 6:
            f6 = element

def change_the_squares_for_AI(part, element):
    global A1, A2, A3, A4, A5, A6, B1, B2, B3, B4, B5, B6, C1, C2, C3, C4, C5, C6, D1, D2, D3, D4, D5, D6, E1, E2, E3, E4, E5, E6, F1, F2, F3, F4, F5, F6
    if part[0] == 1:
        if part[1] == 1:
            A1 = element
        elif part[1] == 2:
            A2 = element
        elif part[1] == 3:
            A3 = element
        elif part[1] == 4:
            A4 = element
        elif part[1] == 5:
            A5 = element
        elif part[1] == 6:
            A6 = element
    elif part[0] == 2:
        if part[1] == 1:
            B1 = element
        elif part[1] == 2:
            B2 = element
        elif part[1] == 3:
            B3 = element
        elif part[1] == 4:
            B4 = element
        elif part[1] == 5:
            B5 = element
        elif part[1] == 6:
            B6 = element
    elif part[0] == 3:
        if part[1] == 1:
            C1 = element
        elif part[1] == 2:
            C2 = element
        elif part[1] == 3:
            C3 = element
        elif part[1] == 4:
            C4 = element
        elif part[1] == 5:
            C5 = element
        elif part[1] == 6:
            C6 = element
    elif part[0] == 4:
        if part[1] == 1:
            D1 = element
        elif part[1] == 2:
            D2 = element
        elif part[1] == 3:
            D3 = element
        elif part[1] == 4:
            D4 = element
        elif part[1] == 5:
            D5 = element
        elif part[1] == 6:
            D6 = element
    elif part[0] == 5:
        if part[1] == 1:
            E1 = element
        elif part[1] == 2:
            E2 = element
        elif part[1] == 3:
            E3 = element
        elif part[1] == 4:
            E4 = element
        elif part[1] == 5:
            E5 = element
        elif part[1] == 6:
            E6 = element
    elif part[0] == 6:
        if part[1] == 1:
            F1 = element
        elif part[1] == 2:
            F2 = element
        elif part[1] == 3:
            F3 = element
        elif part[1] == 4:
            F4 = element
        elif part[1] == 5:
            F5 = element
        elif part[1] == 6:
            F6 = element

class DeskOfThePlayer:
    def __init__(self, a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, c5, c6, d1, d2, d3, d4, d5, d6,
                 e1, e2, e3, e4, e5, e6, f1, f2, f3, f4, f5, f6):
        self.a1, self.a2, self.a3, self.a4, self.a5, self.a6 = a1, a2, a3, a4, a5, a6
        self.b1, self.b2, self.b3, self.b4, self.b5, self.b6 = b1, b2, b3, b4, b5, b6
        self.c1, self.c2, self.c3, self.c4, self.c5, self.c6 = c1, c2, c3, c4, c5, c6
        self.d1, self.d2, self.d3, self.d4, self.d5, self.d6 = d1, d2, d3, d4, d5, d6
        self.e1, self.e2, self.e3, self.e4, self.e5, self.e6 = e1, e2, e3, e4, e5, e6
        self.f1, self.f2, self.f3, self.f4, self.f5, self.f6 = f1, f2, f3, f4, f5, f6

    def draw(self):
        global a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, c5, c6, d1, d2, d3, d4, d5, d6, e1, e2, e3, e4, e5, e6, f1, f2, f3, f4, f5, f6
        list_of_squares = [[a1, a2, a3, a4, a5, a6], [b1, b2, b3, b4, b5, b6], [c1, c2, c3, c4, c5, c6],
                           [d1, d2, d3, d4, d5, d6], [e1, e2, e3, e4, e5, e6], [f1, f2, f3, f4, f5, f6]]
        print('Ваше поле:')
        print('   | 1 | 2 | 3 | 4 | 5 | 6 |')
        j = 1
        for i in list_of_squares:
            print(f' {j} | {i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]} |')
            j += 1

    def add_ship(self, length, dot_of_the_nose, direction):
        global a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, c5, c6, d1, d2, d3, d4, d5, d6, e1, e2, e3, e4, e5, e6, f1, f2, f3, f4, f5, f6, move, moves_by_the_player

        while True:
            if length == 1:
                if 1 <= dot_of_the_nose[0] <= 6 and 1 <= dot_of_the_nose[1] <= 6 and len(dot_of_the_nose) == 2:
                    break
                else:
                    print("Ошибка при введении координат. Повторите попытку.")
                    dot_of_the_nose = list(map(int, input().split()))
                    direction = 'h'
            elif direction == 'v':
                if 1 <= dot_of_the_nose[0] <= 6 and 1 <= dot_of_the_nose[1] <= 6 and 1 <= dot_of_the_nose[0] + length - 1 <= 6 and len(dot_of_the_nose) == 2:
                    break
                else:
                    print("Ошибка при введении координат. Повторите попытку.")
                    dot_of_the_nose = list(map(int, input().split()))
                    direction = input().lower()

            elif direction == 'h':
                if 1 <= dot_of_the_nose[0] <= 6 and 1 <= dot_of_the_nose[1] <= 6 and 1 <= dot_of_the_nose[1] + length - 1 <= 6 and len(dot_of_the_nose) == 2:
                    break
                else:
                    print("Ошибка при введении координат. Повторите попытку.")
                    dot_of_the_nose = list(map(int, input().split()))
                    direction = input().lower()
            else:
                print("Ошибка при введении направления. Повторите попытку.")
                dot_of_the_nose = list(map(int, input().split()))
                direction = input().lower()

        while True:
            flag = True
            for i in range(length):
                if length == 1:
                    if [dot_of_the_nose[0] + i, dot_of_the_nose[1]] in space_for_the_player:
                        print("Рядом уже стоят корабли. Повторите попытку.")
                        dot_of_the_nose = list(map(int, input().split()))
                        direction = 'h'
                        flag = False
                        break
                elif direction == 'v':
                    if [dot_of_the_nose[0] + i, dot_of_the_nose[1]] in space_for_the_player:
                        print("Рядом уже стоят корабли. Повторите попытку.")
                        dot_of_the_nose = list(map(int, input().split()))
                        direction = input().lower()
                        flag = False
                        break
                elif direction == 'h':
                    if [dot_of_the_nose[0], dot_of_the_nose[1] + i] in space_for_the_player:
                        print("Рядом уже стоят корабли. Повторите попытку.")
                        dot_of_the_nose = list(map(int, input().split()))
                        direction = input().lower()
                        flag = False
                        break
            if flag == True:
                break


        for _ in range(length):
            change_the_squares_for_player(dot_of_the_nose, '■')

            space_for_the_player.append([dot_of_the_nose[0], dot_of_the_nose[1] + 1])
            space_for_the_player.append([dot_of_the_nose[0], dot_of_the_nose[1]])
            space_for_the_player.append([dot_of_the_nose[0] - 1, dot_of_the_nose[1]])
            space_for_the_player.append([dot_of_the_nose[0] + 1, dot_of_the_nose[1]])
            space_for_the_player.append([dot_of_the_nose[0], dot_of_the_nose[1] - 1])

            if direction == 'v':
                dot_of_the_nose[0] += 1
            elif direction == 'h':
                dot_of_the_nose[1] += 1

        if direction == 'v':
            for j in range(length):
                ships_of_the_player.append([dot_of_the_nose[0] + j - length, dot_of_the_nose[1]])
        elif direction == 'h':
            for j in range(length):
                ships_of_the_player.append([dot_of_the_nose[0], dot_of_the_nose[1] + j - length])

    def shot(self, shot):
        while True:
            if 1 <= shot[0] <= 6 and 1 <= shot[1] <= 6 and shot not in moves_by_the_player:
                break
            elif shot in moves_by_the_player:
                print('Выстрел уже был произведен на это поле. Повторите снова')
                shot = list(map(int, input().split()))
            else:
                print('Неверные координаты выстрела. Повторите снова')
                shot = list(map(int, input().split()))

        if shot in ships_of_the_AI:
            change_the_squares_for_AI(shot, 'X')
            success_moves_by_the_player.append(shot)
        elif shot not in ships_of_the_AI:
            change_the_squares_for_AI(shot, '.')
        moves_by_the_player.append(shot)



class DeskOfTheAI:
    def __init__(self, A1, A2, A3, A4, A5, A6, B1, B2, B3, B4, B5, B6, C1, C2, C3, C4, C5, C6, D1, D2, D3, D4, D5, D6,
                 E1, E2, E3, E4, E5, E6, F1, F2, F3, F4, F5, F6):
        self.A1, self.A2, self.A3, self.A4, self.A5, self.A6 = A1, A2, A3, A4, A5, A6
        self.B1, self.B2, self.B3, self.B4, self.B5, self.B6 = B1, B2, B3, B4, B5, B6
        self.C1, self.C2, self.C3, self.C4, self.C5, self.C6 = C1, C2, C3, C4, C5, C6
        self.D1, self.D2, self.D3, self.D4, self.D5, self.D6 = D1, D2, D3, D4, D5, D6
        self.E1, self.E2, self.E3, self.E4, self.E5, self.E6 = E1, E2, E3, E4, E5, E6
        self.F1, self.F2, self.F3, self.F4, self.F5, self.F6 = F1, F2, F3, F4, F5, F6

    def draw(self):
        global A1, A2, A3, A4, A5, A6, B1, B2, B3, B4, B5, B6, C1, C2, C3, C4, C5, C6, D1, D2, D3, D4, D5, D6, E1, E2, E3, E4, E5, E6, F1, F2, F3, F4, F5, F6
        list_of_AI_squares = [[A1, A2, A3, A4, A5, A6], [B1, B2, B3, B4, B5, B6], [C1, C2, C3, C4, C5, C6],
                           [D1, D2, D3, D4, D5, D6], [E1, E2, E3, E4, E5, E6], [F1, F2, F3, F4, F5, F6]]
        print('Поле ИИ:')
        print('   | 1 | 2 | 3 | 4 | 5 | 6 |')
        j = 1
        for i in list_of_AI_squares:
            print(f' {j} | {i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]} |')
            j += 1

    def add_ship(self, length, dot_of_the_nose, direction):
        while True:
            flag = True
            for i in range(length):
                if direction == 'v':
                    if ([dot_of_the_nose[0], dot_of_the_nose[1] + i] in space_for_the_AI or 1 > dot_of_the_nose[0] + i or
                            1 > dot_of_the_nose[1] + i or 6 < dot_of_the_nose[0] + i or 6 < dot_of_the_nose[1] + i):
                        dot_of_the_nose = [random.randint(1, 6), random.randint(1, 6)]
                        direction = random.choice(['h', 'v'])
                        flag = False
                        break
                elif direction == 'h':
                    if ([dot_of_the_nose[0] + i, dot_of_the_nose[1]] in space_for_the_AI or 1 > dot_of_the_nose[0] + i or
                    1 > dot_of_the_nose[1] + i or 6 < dot_of_the_nose[0] + i or 6 < dot_of_the_nose[1] + i):
                        dot_of_the_nose = [random.randint(1, 6), random.randint(1, 6)]
                        direction = random.choice(['h', 'v'])
                        flag = False
                        break
            if flag == True:
                break

        if direction == 'h':
            for j in range(length):
                ships_of_the_AI.append([dot_of_the_nose[0] + j, dot_of_the_nose[1]])
                space_for_the_AI.append([dot_of_the_nose[0] + j, dot_of_the_nose[1] + 1])
                space_for_the_AI.append([dot_of_the_nose[0] + j, dot_of_the_nose[1]])
                space_for_the_AI.append([dot_of_the_nose[0] - 1 + j, dot_of_the_nose[1]])
                space_for_the_AI.append([dot_of_the_nose[0] + 1 + j, dot_of_the_nose[1]])
                space_for_the_AI.append([dot_of_the_nose[0] + j, dot_of_the_nose[1] - 1])
        elif direction == 'v':
            for j in range(length):
                ships_of_the_AI.append([dot_of_the_nose[0], dot_of_the_nose[1] + j])
                space_for_the_AI.append([dot_of_the_nose[0], dot_of_the_nose[1] + 1 + j])
                space_for_the_AI.append([dot_of_the_nose[0], dot_of_the_nose[1] + j])
                space_for_the_AI.append([dot_of_the_nose[0] - 1, dot_of_the_nose[1] + j])
                space_for_the_AI.append([dot_of_the_nose[0] + 1, dot_of_the_nose[1] + j])
                space_for_the_AI.append([dot_of_the_nose[0], dot_of_the_nose[1] - 1 + j])

    def shot(self, coordinate):
        while True:
            if coordinate not in moves_by_the_AI:
                break
            else:
                coordinate = [random.randint(1, 6), random.randint(1, 6)]
        if coordinate in ships_of_the_player:
            change_the_squares_for_player(coordinate, 'X')
            success_moves_by_the_AI.append(coordinate)
        elif coordinate not in ships_of_the_player:
            change_the_squares_for_player(coordinate, '.')
        moves_by_the_AI.append(coordinate)

def game_rules():
    print("Здравствуйте! Добро пожаловать в игру морской бой. Правила игры следующие:",
          "Сначала нужно поставить свои корабли на доску. Вводите координаты  корабля в консоль.",
          "Через пробел введите координаты носа корабля и нажмите после Enter. Далее введите направление корабля.",
          "Чтобы поставить корабль вертикально или горизонтально, введите v или h, соответственно.",
          "В общем у вас и у компьютера будет 1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку.",
          "Все корабли обязательно должны стоять внутри доски и находиться минимум на расстоянии 1 клетки друг от друга.",
          "После растановки кораблей у вас будет задача уничтожить все корабли противника. 1 ход - 1 выстрел.",
          "Побеждает тот, кто первым уничтожит все корабли противника.",
          'Подбитые корабли помечаются как "Х", а промахи как ".".', "Удачи!", sep='\n')


desk_of_the_player = DeskOfThePlayer(a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, c5, c6, d1, d2, d3,
                                     d4, d5, d6, e1, e2, e3, e4, e5, e6, f1, f2, f3, f4, f5, f6)
desk_of_the_AI = DeskOfTheAI(A1, A2, A3, A4, A5, A6, B1, B2, B3, B4, B5, B6, C1, C2, C3, C4, C5, C6, D1, D2, D3, D4, D5,
                             D6, E1, E2, E3, E4, E5, E6, F1, F2, F3, F4, F5, F6)

space_for_the_player, moves_by_the_player, ships_of_the_player, success_moves_by_the_player = [], [], [], []

space_for_the_AI, moves_by_the_AI, ships_of_the_AI, success_moves_by_the_AI = [], [], [], []

#   Начало игры
game_rules()
desk_of_the_player.draw()
#   Растановка кораблей игрока
while True:
    move = list(map(int, input().split()))
    dire = input().lower()
    desk_of_the_player.add_ship(3, move, dire)
    desk_of_the_player.draw()
    for i in range(2):
        move = list(map(int, input().split()))
        dire = input().lower()
        desk_of_the_player.add_ship(2, move, dire)
        desk_of_the_player.draw()
    for i in range(4):
        move = list(map(int, input().split()))
        desk_of_the_player.add_ship(1, move, 'h')
        desk_of_the_player.draw()
    break

#   Растановка кораблей ИИ
while True:
    AI_move = [random.randint(1, 6), random.randint(1, 6)]
    direction = random.choice(['h', 'v'])
    desk_of_the_AI.add_ship(3, AI_move, direction)
    for i in range(2):
        AI_move = [random.randint(1, 6), random.randint(1, 6)]
        direction = random.choice(['h', 'v'])
        desk_of_the_AI.add_ship(2, AI_move, direction)
    for i in range(4):
        AI_move = [random.randint(1, 6), random.randint(1, 6)]
        desk_of_the_AI.add_ship(1, AI_move, 'h')
    desk_of_the_AI.draw()
    break

#   Сама игра
print('Сделайте выстрел, написав координаты выстрела через пробел')
while True:
    shot = list(map(int, input().split()))
    desk_of_the_player.shot(shot)
    making_a_AI_move = [random.randint(1, 6), random.randint(1, 6)]
    desk_of_the_AI.shot(making_a_AI_move)
    desk_of_the_player.draw()
    desk_of_the_AI.draw()
    if sorted(success_moves_by_the_AI) == sorted(ships_of_the_player) and sorted(success_moves_by_the_player) == sorted(ships_of_the_AI):
        print('Все корабли ИИ и игрока пробиты. Ничья. Игра окончена.')
        break
    elif sorted(success_moves_by_the_AI) == sorted(ships_of_the_player):
        print('Все корабли игрока пробиты. ИИ победил. Игра окончена.')
        break
    elif sorted(success_moves_by_the_player) == sorted(ships_of_the_AI):
        print('Все корабли ИИ пробиты. Игрок победил. Игра окончена.')
        break