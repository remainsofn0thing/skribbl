class Board(object):
    ROWS = COLS = 720

    def __init__(self):
        """
        init board by crating empty board / pixels all white
        """
        self.data = self._create_empty_board()

    def update(self, x, y, color):
        """
        updates a singular pixel on the board
        :param x:int
        :param y:int
        :param color:(int,int,int)
        :return:
        """
        self.data[y][x] = color

    def _create_empty_board(self):
        """
        creates empty board / pixels all white
        :return:None
        """
        return [[(255, 255, 255) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def clear(self):
        """
        clear all board to white color
        :return:None
        """
        self.data = self._create_empty_board()

    def fill(self, x, y):
        """
        fills in a specific shape of area using recursion
        :param x: int
        :param y: int
        :return: None
        """
        pass

    def get_board(self):
        """
        gets the data of the board
        :return: (int,int,int)[]
        """
        return self.data
