from btnode import Node
from board import Board
import random
import copy


class Tree:
    def __init__(self, base_data):
        self.root = Node(base_data)

    def check(self):
        result = 0
        state = self.root.data.check()
        if state[0]:
            if state[1] == "x":
                return -1
            elif state[1] == "0":
                return 1
            elif state[1] == "draw":
                return 0
        if self.root.right is not None:
            result += self.root.right.check()
        if self.root.left is not None:
            result += self.root.left.check()
        return result

    def generate(self):
        if not self.root.data.check()[0]:
            if self.root.right is None:
                free = []
                for j in range(3):
                    for n in range(3):
                        if self.root.data.state[j][n] == "_":
                            free.append((j, n))
                if len(free) > 0:
                    tile = random.choice(free)
                    new_row = ""
                    for j in range(3):
                        if j != tile[1]:
                            new_row += self.root.data.state[tile[0]][j]
                        elif self.root.data.last_turn == "x":
                            new_row += "0"
                        elif self.root.data.last_turn == "0":
                            new_row += "x"
                    self.root.right = Tree(Board())
                    self.root.right.root.data.state = copy.deepcopy(self.root.data.state)
                    self.root.right.root.data.state[tile[0]] = new_row
                    if self.root.data.last_turn == "x":
                        self.root.right.root.data.last_turn = "0"
                    elif self.root.data.last_turn == "0":
                        self.root.right.root.data.last_turn = "x"
                    self.root.right.generate()
            if self.root.left is None:
                free = []
                for j in range(3):
                    for n in range(3):
                        if self.root.data.state[j][n] == "_":
                            free.append((j, n))
                if len(free) > 0:
                    tile = random.choice(free)
                    new_row = ""
                    for j in range(3):
                        if j != tile[1]:
                            new_row += self.root.data.state[tile[0]][j]
                        elif self.root.data.last_turn == "x":
                            new_row += "0"
                        elif self.root.data.last_turn == "0":
                            new_row += "x"
                    self.root.left = Tree(Board())
                    self.root.left.root.data.state = copy.deepcopy(self.root.data.state)
                    self.root.left.root.data.state[tile[0]] = new_row
                    if self.root.data.last_turn == "x":
                        self.root.left.root.data.last_turn = "0"
                    elif self.root.data.last_turn == "0":
                        self.root.left.root.data.last_turn = "x"
                    self.root.left.generate()
