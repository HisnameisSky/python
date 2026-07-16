import abc
import random


class Player(abc.ABC):

    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        chosen_move = random.choice(self.moves)

        new_x = self.position[0] + chosen_move[0]
        new_y = self.position[1] + chosen_move[1]

        self.position = (new_x, new_y)
        self.path.append(self.position)

        return self.position

    @abc.abstractmethod
    def level_up(self) -> None:
        pass


class Pawn(Player):

    def __init__(self) -> None:
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self) -> None:
        
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonal_moves)