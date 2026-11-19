# Chess Engine

A Python chess engine that runs in the terminal.

* Searches moves with negamax and alpha-beta pruning.
* Scores positions using piece values and piece-square tables.
* Uses a configurable search depth, currently set to 10.
* Prints the board after each move.
* Supports engine matches or human turns through flags in `board.py`.
* Accepts UCI moves on human turns.
* Detects checkmate, stalemate, insufficient material, repetition, and move-limit draws.
