import random

scores = {"r": -5,
          "R": 5,
          "n": -3,
          "N": 3,
          "b": -3,
          "B": 3,
          "q": -10,
          "Q": 10,
          "p":-1,
          "P":1,
          "k":0,
          "K":0}

CHECKMATE = 1000
STALEMATE = 0

def getRandomMove(board, legalMoves):
    rNum = random.randrange(0, len(legalMoves))
    board.push(legalMoves[rNum])


def scoreBoard(board):
    score = 0
    for i in range(64):
        if board.piece_at(i) == None:
            continue
        else:
            score += scores[str(board.piece_at(i))]
    return score

def findBestMove(board, legalMoves, whiteToPlay):
    turnMultiplier = 1 if whiteToPlay else -1
    opponentMinMaxScore = CHECKMATE
    bestPlayerMove = None
    random.shuffle(legalMoves)
    for move in legalMoves:
        board.push(move)
        possibleOpponentMoves = list(board.legal_moves)
        opponentMaxScore = -CHECKMATE
        for possibleOpponentMove in possibleOpponentMoves:
            board.push(possibleOpponentMove)
            if board.is_checkmate():
                currScore = -turnMultiplier * CHECKMATE
            elif board.is_stalemate():
                currScore = STALEMATE
            else:
                currScore = -turnMultiplier * scoreBoard(board)
            if currScore > opponentMaxScore:
                opponentMaxScore = currScore
            board.pop()
        if opponentMinMaxScore > opponentMaxScore:
            opponentMinMaxScore = opponentMaxScore
            bestPlayerMove = move
        board.pop()
    return bestPlayerMove

