from stockfish import Stockfish

stockfish = Stockfish(r'C:\Users\Fgtfv567\Documents\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe', depth = 18, parameters ={"Threads": 2, "Minimum Thinking Time": 30})

#stockfish = Stockfish(r'C:\Users\Fgtfv567\Documents\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe', depth=18, parameters={"Threads": 2, "Minimum Thinking Time": 30})
fen_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
chess_width = 8
chess_height = 8

stockfish.set_fen_position(fen_position) #New Game
#stockfish.set_fen_position("3k4/5P2/8/8/8/8/8/3K4 w - - 0 1") #pawn to be queened
#stockfish.set_fen_position("k7/5P2/8/8/8/8/4p3/1K6 b - - 0 1")
#stockfish.set_fen_position("8/8/8/3p4/4P3/8/8/8") #2 pawns enter, 1 pawn lives

def fen_to_2d_array(fen_string):
    board_fen = [fen_string]
    split_board = board_fen[0].split('/')
    final_board = []
    for row in split_board:
        if row[0] == '8':
            final_board.append(['--'] * 8)
        else:
            board_row = [(row[i: i+1]) for i in range(0, len(row), 1)]
            final_board.append(board_row)
    return final_board

chess_board_2d = fen_to_2d_array(fen_position)
chess_coordinate_system_to_array_index_row = [x for x in range(chess_height-1, -1, -1)]
chess_coordinate_system_to_array_index_column = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}

def chess_board_2d_move(direction):
    origin_row = direction[1]
    origin_column = direction[0]
    target_row = direction[3]
    target_column = direction[2]
    origin_piece = chess_board_2d[chess_coordinate_system_to_array_index_row[int(origin_row)-1]][chess_coordinate_system_to_array_index_column[origin_column]]

    chess_board_2d[chess_coordinate_system_to_array_index_row[int(origin_row)-1]][chess_coordinate_system_to_array_index_column[origin_column]] = '--'

    chess_board_2d[chess_coordinate_system_to_array_index_row[int(target_row)-1]][chess_coordinate_system_to_array_index_column[target_column]] = origin_piece

def split_input(input):
    return input[2] + input[3]

def is_capture(position):
    row = position[1]
    column = position[0]
    return not chess_board_2d[chess_coordinate_system_to_array_index_row[int(row)-1]][chess_coordinate_system_to_array_index_column[column]] == "--"

# print("Game Start")
# print("You are the player top of the board!")
print(stockfish.get_board_visual())
while True:

#Player input
    playerinput = input() #Enter string\n
    # print(playerinput)

    # print(stockfish.is_move_correct(playerinput))
    while True:
        if stockfish.is_move_correct(playerinput):
            playertarget = split_input(playerinput)
            # print("Capture result is: " + playertarget)
            # print(is_capture(playertarget))
            # if is_capture(playertarget):
            #     print('k' + playerinput)
            stockfish.make_moves_from_current_position([playerinput])
            chess_board_2d_move(playerinput)
            break
        elif not stockfish.is_move_correct(playerinput):
            playerinput = input() #Re-enter string\n

    # playertarget = split_input(playerinput)
    # print("Capture result is: " + playertarget)
    # print(is_capture(playertarget))
    # print("Player Moved:")
    # print(stockfish.get_board_visual())

#Robot input
    #print(stockfish.get_best_move(wtime=None, btime=1000))
    robotinput = stockfish.get_best_move(wtime=None, btime=1000)


    robottarget = split_input(robotinput)
    # print("Capture result is: " + robottarget)
    # print(is_capture(robottarget))
    if is_capture(robottarget):
        print('k' + robotinput)
    else:
        print(robotinput)

    chess_board_2d_move(robotinput)
    stockfish.make_moves_from_current_position([robotinput])



    # print("Capture result is: " + robottarget)
    # print(is_capture(robottarget))
    # print("Robot Moved:")
    # print(stockfish.get_board_visual())
    #
    # print(stockfish.get_evaluation())

    # for row in chess_board_2d:
    #     print(row)

#Check for Checkmate
    # checkmate = stockfish.get_evaluation().get("type")
    # if checkmate == "mate":
    #     print("Checkmate!")


#Comments below
#stockfish = Stockfish(r'C:\Users\Fgtfv567\Documents\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe', depth=18, parameters={"Threads": 2, "Minimum Thinking Time": 30})
#print(stockfish.get_board_visual())

# set position by FEN:
#stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")

#p1 = "e2"
#p2 = "e4"
# set position by moves:
#stockfish.set_position([p1+p2])

#print(stockfish.get_board_visual())

#input = "a2a3"
#print(stockfish.is_move_correct(input))

#print(stockfish.get_best_move()) # d2d4
#print(stockfish.is_move_correct('a2a3')) # True

#stockfish.get_fen_position()
#print(stockfish.get_board_visual())

#Tells me that there is a turn system that must be followed, lowercase goes first
"""while True:
    print(stockfish.get_board_visual())
#Player input
    playerinput = input("Enter string\n")
    print(playerinput)
    print(stockfish.is_move_correct(playerinput))
    stockfish.make_moves_from_current_position([playerinput])
    print("Player moved")"""