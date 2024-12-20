from typing import List

import chess
import chess.svg
# from IPython.display import display
from typing_extensions import Annotated

# Initialize the board.
board = chess.Board()
print('➡ chess_agents.py:10 board:', board)

# Keep track of whether a move has been made.
made_move = False

print(board.legal_moves)


# def get_legal_moves() -> Annotated[str, "A list of legal moves in UCI format"]:
#     return "Possible moves are: " + ",".join([str(move) for move in board.legal_moves])


# def make_move(move: Annotated[str, "A move in UCI format."]) -> Annotated[str, "Result of the move."]:
#     move = chess.Move.from_uci(move)
#     board.push_uci(str(move))
#     global made_move
#     made_move = True
#     # Display the board.
#     display(
#         chess.svg.board(board, arrows=[(move.from_square, move.to_square)], fill={move.from_square: "gray"}, size=200)
#     )
#     # Get the piece name.
#     piece = board.piece_at(move.to_square)
#     piece_symbol = piece.unicode_symbol()
#     piece_name = (
#         chess.piece_name(piece.piece_type).capitalize()
#         if piece_symbol.isupper()
#         else chess.piece_name(piece.piece_type)
#     )
#     return f"Moved {piece_name} ({piece_symbol}) from {chess.SQUARE_NAMES[move.from_square]} to {chess.SQUARE_NAMES[move.to_square]}."
