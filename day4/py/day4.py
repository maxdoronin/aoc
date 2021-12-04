import copy

board_size = 5

def parse_boards(lines):
    boards = [[],[]]
    while len(lines) > 0:
        lines.pop(0)
        board = []
        result = []
        while len(lines) > 0 and lines[0].strip() != '':
            board_line = [int(n) for n in lines.pop(0).strip().split()]
            board.append(board_line)
            result.append(0)
        boards[0].append(board)
        boards[1].append([[0]*board_size for i in range(board_size)])
    return(boards)

def read_input(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        numbers = [int(n) for n in lines.pop(0).strip().split(',')]
        boards = parse_boards(lines)
        return (numbers, boards)

def board_has_won(result):
    for line in result:
        if sum(line) == board_size:
            return(True)
    col_sums = [sum(col) for col in zip(*result)]
    for col in col_sums:
        if col == board_size:
            return(True)
    return (False)

def check_number_part_1(boards, pick):
    for board_no, board in enumerate(boards[0]):
        for board_line_no, board_line in enumerate(board):
            for number_no, number in enumerate(board_line):
                if number == pick:
                    # print ('Number {} present at {}-{}-{}'.format(pick,board_no,board_line_no,number_no))
                    boards[1][board_no][board_line_no][number_no] = 1
                    if board_has_won(boards[1][board_no]):
                        return (boards, board_no)
    return (boards, None)

def check_number_part_2(boards, pick, win_snapshot, break_on_win=False):
    for board_no, board in enumerate(boards[0]):
        for board_line_no, board_line in enumerate(board):
            for number_no, number in enumerate(board_line):
                if number == pick:
                    # print ('Number {} present at {}-{}-{}'.format(pick,board_no,board_line_no,number_no))
                    if not board_has_won(boards[1][board_no]):
                        boards[1][board_no][board_line_no][number_no] = 1
                        if board_has_won(boards[1][board_no]):
                            win_snapshot = [boards[0][board_no], copy.deepcopy(boards[1][board_no]), pick]
                            if break_on_win:
                                return (boards, win_snapshot)
                    else:
                        boards[1][board_no][board_line_no][number_no] = 1
    return (boards, win_snapshot)

def get_score(board, result):
    score_card = [[board[i][j] * (1 - result[i][j]) for j in range(board_size)] for i in range(board_size)]
    score = sum([sum(col) for col in zip(*score_card)])
    return (score)

def game_part_1(numbers, boards):
    for pick in numbers:
        (boards, winning_board) = check_number_part_1(boards, pick)
        if winning_board != None:
            score = get_score(boards[0][winning_board], boards[1][winning_board])
            print ('{}*{}={}'.format(score, pick, score*pick))
            break

def game_part_1_1(numbers, boards):
    win_snapshot = [[],[],None]
    for pick in numbers:
        (boards, win_snapshot) = check_number_part_2(boards, pick, win_snapshot, True)
        if win_snapshot[2] != None:
            score = get_score(win_snapshot[0], win_snapshot[1])
            print ('{}*{}={}'.format(score, win_snapshot[2], score*win_snapshot[2]))
            break

def game_part_2(numbers, boards):
    win_snapshot = [[],[],None]
    for pick in numbers:
        (boards, win_snapshot) = check_number_part_2(boards, pick, win_snapshot)
    score = get_score(win_snapshot[0], win_snapshot[1])
    print ('{}*{}={}'.format(score, win_snapshot[2], score*win_snapshot[2]))

(numbers, boards) = read_input('../testinput.txt')
game_part_1(numbers, boards)
(numbers, boards) = read_input('../testinput.txt')
game_part_1_1(numbers, boards)
(numbers, boards) = read_input('../testinput.txt')
game_part_2(numbers, boards)

(numbers, boards) = read_input('../input.txt')
game_part_1(numbers, boards)
(numbers, boards) = read_input('../input.txt')
game_part_1_1(numbers, boards)
(numbers, boards) = read_input('../input.txt')
game_part_2(numbers, boards)