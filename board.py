class Board:
    def __init__(self):
        self.state = ["___", "___", "___"]
        self.last_turn = "0"

    def check(self):
        for i in range(3):
            if self.state[0][i] == self.state[1][i] == self.state[2][i] and self.state[0][i] != "_":
                return True, self.state[0][i]
            elif self.state[i] == "xxx" or self.state[i] == "000":
                return True, self.state[i][0]
        if self.state[0][0] == self.state[1][1] == self.state[2][2] != "_":
            return True, self.state[1][1]
        elif self.state[0][-1] == self.state[1][-2] == self.state[2][-3] != "_":
            return True, self.state[1][1]
        for i in range(3):
            if self.state[i][0] == "_" or self.state[i][1] == "_" or self.state[i][2] == "_":
                return False, "continue"
        return True, "draw"

    def show_board(self):
        print("\n".join(self.state))
