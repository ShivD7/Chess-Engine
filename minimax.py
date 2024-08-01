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

knightScore = [1, 1, 1, 1, 1, 1, 1, 1,
               1, 2, 2, 2, 2, 2, 2, 1,
               1, 2, 3, 3, 3, 3, 2, 1,
               1, 2, 3, 4, 4, 3, 2, 1,
               1, 2, 3, 4, 4, 3, 2, 1,
               1, 2, 3, 3, 3, 3, 2, 1,
               1, 2, 2, 2, 2, 2, 2, 1,
               1, 1, 1, 1, 1, 1, 1, 1]

bishopScores = [4, 3, 2, 1, 1, 2, 3, 4,
                3, 4, 3, 2, 2, 3, 4, 3,
                2, 3, 4, 3, 3, 4, 3, 2,
                1, 2, 3, 4, 4, 3, 2, 1,
                1, 2, 3, 4, 4, 3, 2, 1,
                2, 3, 4, 3, 3, 4, 3, 2,
                3, 4, 3, 2, 2, 3, 4, 3,
                4, 3, 2, 1, 1, 2, 3, 4]

queenScores = [1, 1, 1, 3, 1, 1, 1, 1,
               1, 2, 3, 3, 3, 1, 1, 1,
               1, 4, 3, 3, 3, 4, 2, 1,
               1, 2, 3, 3, 3, 2, 2, 1,
               1, 2, 3, 3, 3, 2, 2, 1,
               1, 4, 3, 3, 3, 4, 2, 1,
               1, 2, 3, 3, 3, 1, 1, 1,
               1, 1, 1, 3, 1, 1, 1, 1]

rookScores = [4, 3, 4, 4, 4, 4, 3, 4,
              4, 4, 4, 4, 4, 4, 4, 4,
              1, 1, 2, 3, 3, 2, 1, 1,
              1, 2, 3, 4, 4, 3, 2, 1,
              1, 2, 3, 4, 4, 3, 2, 1,
              1, 1, 2, 3, 3, 2, 1, 1,
              4, 4, 4, 4, 4, 4, 4, 4,
              4, 3, 4, 4, 4, 4, 3, 4]

whitePawnScores = [8, 8, 8, 8, 8, 8, 8, 8,
                   8, 8, 8, 8, 8, 8, 8, 8,
                   5, 6, 6, 7, 7, 6, 6, 5,
                   2, 3, 3, 5, 5, 3, 3, 2,
                   1, 2, 3, 4, 4, 3, 2, 1,
                   1, 1, 2, 3, 3, 2, 1, 1,
                   1, 1, 1, 0, 0, 1, 1, 1,
                   0, 0, 0, 0, 0, 0, 0, 0]

blackPawnScores = [0, 0, 0, 0, 0, 0, 0, 0,
                   1, 1, 1, 0, 0, 1, 1, 1,
                   1, 1, 2, 3, 3, 2, 1, 1,
                   1, 2, 3, 4, 4, 3, 2, 1,
                   2, 3, 3, 5, 5, 3, 3, 2,
                   5, 6, 6, 7, 7, 6, 6, 5,
                   8, 8, 8, 8, 8, 8, 8, 8,
                   8, 8, 8, 8, 8, 8, 8, 8]

piecePositionScores = {"N":knightScore, "Q": queenScores, "B": bishopScores, "R": rookScores, "P": whitePawnScores, "p": blackPawnScores}

CHECKMATE = 1000
STALEMATE = 0
DEPTH = 10

def getRandomMove(board, legalMoves):
    rNum = random.randrange(0, len(legalMoves))
    board.push(legalMoves[rNum])


def findBestMove(board, legalMoves, whiteToPlay):
    global nextMove
    nextMove = None
    findMoveNegaMaxAlphaBeta(board, legalMoves, DEPTH, -CHECKMATE, CHECKMATE, 1 if whiteToPlay else -1)
    return nextMove
    
def findMoveNegaMaxAlphaBeta(board, legalMoves, depth, alpha, beta, multiplier):
    global nextMove
    if depth == 0:
        return multiplier * scoreBoard(board, True if multiplier == 1 else False)
    

    maxScore = -CHECKMATE
    random.shuffle(legalMoves)
    for move in legalMoves:
        board.push(move)
        nextMoves = list(board.legal_moves)
        score = -findMoveNegaMaxAlphaBeta(board, nextMoves, depth - 1, -beta, -alpha, -multiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
                print(move, score)
        board.pop()
        if maxScore > alpha: #pruning
            alpha = maxScore
        
        if alpha >= beta:
            break
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
        if board.piece_at(i) != None:
            piecePositionScore = 0
            if str(board.piece_at(i)) != "K" and str(board.piece_at(i)) != "k":
                if str(board.piece_at(i)) == "p" or str(board.piece_at(i)) == "P":
                    piecePositionScore = piecePositionScores[str(board.piece_at(i))][i]
                else:
                    piecePositionScore = piecePositionScores[str(board.piece_at(i)).upper()][i]
            score += scores[str(board.piece_at(i))] + piecePositionScore * .1
    return score