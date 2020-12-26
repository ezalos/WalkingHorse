import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def fill_line(board, pos, direc, length):
    if direc == 0:
        x_add = 1
        y_add = 0
    elif direc == 1:
        x_add = 0
        y_add = 1
    elif direc == 2:
        x_add = -1
        y_add = 0
    elif direc == 3:
        x_add = 0
        y_add = -1
    val = board[pos[0]][pos[1]]
    for i in range(length):
        val += 1
        pos[0] += x_add
        pos[1] += y_add
        board[pos[0]][pos[1]] = val
    #return pos

def create_board(size):
    board = [[0 for i in range(size)] for j in range(size)]
    middle = (int((size - 1) / 2))
    pos = [middle, middle]
    board[pos[0]][pos[1]] = 1
    length = 1
    end = False
    while not end:
        for d in range(4):
            fill_line(board, pos, d, length)
            if d % 2 == 1:
                length += 1
            if board[pos[0]][pos[1]] == size * (size - 1) + 1:
                length -= 1
            if board[pos[0]][pos[1]] == size * size:
                end = True
                break
    return board

class WalkingHorse():
    def __init__(self, size):
        self.board = create_board(size)
        self.use = [[0 for i in range(size)] for j in range(size)]
        self.maximum = size * size
        middle = (int((size - 1) / 2))
        self.pos = [middle, middle]
        self.use[middle][middle] = 1
        self.data = []
        self.data.append([1, middle, middle])

    def walk(self):
        while True:
            ret = self.min()
            if not ret:
                break
            self.data.append(ret)

    def min(self):
        add = [1, 2]
        lowest = None
        for n_a in [1, -1]:
            for n_b in [1, -1]:
                for shift in [-1, 0]:
                    x = self.pos[0] + (n_a * add[0 + shift])
                    y = self.pos[1] + (n_b * add[1 + shift])
                    if not self.use[x][y]:
                        val = self.board[x][y]
                        if lowest == None or lowest[0] > val:
                            lowest = [val, x, y]
        if lowest:
            self.use[lowest[1]][lowest[2]] = 1
            self.pos = lowest[1:]
        return lowest

    def graph(self):
        cols = ['value', 'x', 'y'] 
        #df = pd.DataFrame(self.data, columns=cols)
        #print(df)
        v = [i[0] for i in self.data]
        x = [i[1] for i in self.data]
        y = [i[2] for i in self.data]
        #sns.lineplot(x=x, y=y, sort=False)#, hue=v, sort=False)

        plt.plot(x, y)
        plt.show()

    def __str__(self):
        s = len(self.board)
        s = s * s
        s = len(str(s))
        msg = ""
        for line in self.board:
            for c in line:
                if c != 0:
                    msg += "\x1b[{};2;{};{};{}m".format(38, 255, 155, 255)
                msg += "{0:{1}}".format(c, s)
                msg += "\x1b[0m"
                msg += " "
            msg += "\n"
        return msg

if __name__ == "__main__":
    horse = WalkingHorse(60)
    horse.walk()
    horse.graph()

