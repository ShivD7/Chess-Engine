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
DEPTH = 2

def getRandomMove(board, legalMoves):
    rNum = random.randrange(0, len(legalMoves))
    board.push(legalMoves[rNum])


def findBestMove(board, legalMoves, whiteToPlay):
    global nextMove
    nextMove = None
    findMoveNegaMax(board, legalMoves, DEPTH, 1 if whiteToPlay else -1)
    return nextMove
    
"""
def findMoveMinMax(board, legalMoves, depth, whiteToPlay):
    global nextMove
    if depth == 0:
        return scoreMaterial(board)
    
    if whiteToPlay:
        maxScore = -CHECKMATE
        random.shuffle(legalMoves)
        for move in legalMoves:
            board.push(move)
            nextMoves = list(board.legal_moves)
            score = findMoveMinMax(board, nextMoves, depth - 1, False)
            if score > maxScore:
                maxScore = score
                if depth == DEPTH:
                    nextMove = move
            board.pop()
        return maxScore

    else:
        minScore = CHECKMATE
        random.shuffle(legalMoves)
        for move in legalMoves:
            board.push(move)
            nextMoves = list(board.legal_moves)
            score = findMoveMinMax(board, nextMoves, depth - 1, True)
            if score < minScore:
                minScore = score
                if depth == DEPTH:
                    nextMove = move
            board.pop()
        return minScore
"""

def findMoveNegaMax(board, legalMoves, depth, multiplier):
    global nextMove
    if depth == 0:
        return multiplier * scoreBoard(board)
    
    maxScore = -CHECKMATE
    for move in legalMoves:
        board.push(move)
        nextMoves = list(board.legal_moves())
        score = -findMoveNegaMax(board, nextMoves, depth - 1, -multiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
        board.pop()
    return maxScore

def scoreBoard(board, whiteToPlay):
    if board.is_checkmate():
        if whiteToPlay:
            return -CHECKMATE #black wins
        else:
            return CHECKMATE #white wins
    elif board.is_stalemate():
        return STALEMATE
    
    score = 0
    for i in range(64):
        if board.piece_at(i) == None:
            continue
        else:
            score += scores[str(board.piece_at(i))]
    return score


def scoreMaterial(board):
    score = 0
    for i in range(64):
        if board.piece_at(i) == None:
            continue
        else:
            score += scores[str(board.piece_at(i))]
    return score

"""
def findBestMove(board, legalMoves, whiteToPlay):
    turnMultiplier = 1 if whiteToPlay else -1
    opponentMinMaxScore = CHECKMATE
    bestPlayerMove = None
    random.shuffle(legalMoves)
    for move in legalMoves:
        board.push(move)
        possibleOpponentMoves = list(board.legal_moves)
        if board.is_stalemate():
            opponentMaxScore = STALEMATE
        elif board.is_checkmate():
            opponentMaxScore = -CHECKMATE
        else:
            opponentMaxScore = -CHECKMATE
            for possibleOpponentMove in possibleOpponentMoves:
                board.push(possibleOpponentMove)
                list(board.legal_moves)
                if board.is_checkmate():
                    currScore = CHECKMATE
                elif board.is_stalemate():
                    currScore = STALEMATE
                else:
                    currScore = -turnMultiplier * scoreMaterial(board)
                if currScore > opponentMaxScore:
                    opponentMaxScore = currScore
                board.pop()
        if opponentMinMaxScore > opponentMaxScore:
            opponentMinMaxScore = opponentMaxScore
            bestPlayerMove = move
        board.pop()
    return bestPlayerMove
"""
