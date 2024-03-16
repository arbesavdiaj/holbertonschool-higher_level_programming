class Board:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    
    def update(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player.symbol
            return True
        return False
    
    def is_winner(self, player):
        symbol = player.symbol
        for row in self.board:
            if row.count(symbol) == 3:
                return True
            
        for col in range(3):
            if [row[col] for row in self.board].count(symbol) == 3:
                return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True
        return False

class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        
class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = Player('X')
        self.other_player = Player('O')

    def play(self):
        while True:
            self.board.display()
            move = input(f"Player {self.current_player.symbol}, enter your move (row col): ")
            row, col = map(int, move.split())
            if self.board.update(row, col, self.current_player):
                if self.board.is_winner(self.current_player):
                    print(f"Player {self.current_player.symbol} wins!")
                    break
                self.current_player, self.other_player = self.other_player, self.current_player
            else:
                print("Invalid move, try again.")

if __name__ == "__main__":
    Game().play()