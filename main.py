игрокAli_1 = "х"
player_2 = "о"

step_board = list(range(1, 10))

def board():
    print("_____________")
    for n in range(3):
        print("|", step_board[0 + n * 3], "|", step_board[1 + n * 3], "|", step_board[2 + n * 3], "|")
    print("_____________")

def who_win(step_board):
    win_combination = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 5, 8], [2, 4, 6], [3, 4, 5], [6, 7, 8]]
    for w in win_combination:
        if step_board[w[0]] == step_board[w[1]] == step_board[w[2]]:
            return step_board[w[0]]
    return False

def шаг():
    количество = 0
    while количество < 9:
        print("Ход х")
        step_board[int(input("Введите номер установки х: ")) - 1] = "x"
        board()
        if who_win(step_board) == "x":
            print("Поздравляем! Выиграл крестик Ali!")
            return

        if количество == 8:
            print("Ничья! На игровом поле больше нет доступных ходов.")
            return

        print("Ход о")
        step_board[int(input("Введите номер установки о: ")) - 1] = "o"
        board()
        if who_win(step_board) == "o":
            print("Поздравляем! Выиграли нолики!")
            return

        количество += 2

    print("Ничья!.")

шаг()
