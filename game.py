from board import Board
from btree import Tree


class Game:
    def __init__(self):
        self.board = Board()
        self.board.show_board()

    def turn(self):
        if self.board.last_turn == "0":
            coordinates = input("Enter coordinate: ").split()
            if self.board.state[int(coordinates[0])][int(coordinates[1])] != "_":
                raise IndexError
            if int(coordinates[0]) > 2 or int(coordinates[1]) > 2 or 0 > int(coordinates[0]) or 0 > int(coordinates[1]):
                raise IndexError
            new_row = ""
            for j in range(3):
                if j != int(coordinates[1]):
                    new_row += self.board.state[int(coordinates[0])][int(coordinates[0])]
                else:
                    new_row += "x"
            self.board.state[int(coordinates[0])] = new_row
            self.board.last_turn = "x"
        else:
            tree = Tree(self.board)
            tree.generate()
            if tree.root.right.check() > tree.root.left.check():
                self.board = tree.root.right.root.data
            else:
                self.board = tree.root.left.root.data
            self.board.last_turn = "0"
        self.board.show_board()

    def loop(self):
        while not self.board.check()[0]:
            self.turn()

if __name__ == '__main__':
    game = Game()
    game.loop()