import chess
import random
from minimax import getRandomMove, findBestMove

board = chess.Board()
playing = True

player1 = False
player2 = False


counter = 0

while playing:
    whiteToPlay = False
    if counter % 2 == 0:
        whiteToPlay = True
    legalMoves = list(board.legal_moves)
    humanTurn = (whiteToPlay and player1) or (not whiteToPlay and player2)

    if board.is_checkmate() or board.is_stalemate() or board.is_insufficient_material() or board.is_fivefold_repetition() or board.is_seventyfive_moves():
        print(board.is_checkmate(), board.is_stalemate(), board.is_insufficient_material(), board.is_fivefold_repetition(), board.is_seventyfive_moves())
        break
    if humanTurn:
        notation = input("What move would you like to play (please provide valid notation): ")
        move = chess.Move.from_uci(notation)
        board.push(move)
    else:
        move = findBestMove(board, legalMoves, whiteToPlay)
        if move == None:
            getRandomMove(board, legalMoves)
        else:
            board.push(move)
    print(str(board) + "\n")

    counter += 1
