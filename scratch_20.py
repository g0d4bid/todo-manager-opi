import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QGridLayout, QPushButton, QLabel,
                             QRadioButton)
from PyQt5.QtCore import Qt

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.game_active = True
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Крестики-нолики')
        self.setGeometry(300, 300, 700, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        player_layout = QHBoxLayout()
        player_layout.addWidget(QLabel("Первый игрок:"))
        self.x_radio = QRadioButton("X")
        self.o_radio = QRadioButton("O")
        self.x_radio.setChecked(True)
        self.x_radio.toggled.connect(self.new_game)
        self.o_radio.toggled.connect(self.new_game)
        player_layout.addWidget(self.x_radio)
        player_layout.addWidget(self.o_radio)
        layout.addLayout(player_layout)

        grid = QGridLayout()
        self.button_grid = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                btn = QPushButton('')
                btn.setFixedSize(100, 100)
                btn.clicked.connect(lambda _, x=i, y=j: self.make_move(x, y))
                self.button_grid[i][j] = btn
                grid.addWidget(btn, i, j)
        layout.addLayout(grid)

        self.result = QLabel("Ход игрока X")
        self.result.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result)

        self.new_game_button = QPushButton("Новая игра")
        self.new_game_button.clicked.connect(self.new_game)
        layout.addWidget(self.new_game_button)

    def make_move(self, row, col):
        if not self.game_active or self.button_grid[row][col].text():
            return

        self.button_grid[row][col].setText(self.current_player)
        self.board[row][col] = self.current_player

        if self.check_win():
            self.game_active = False
            self.result.setText(f"Выиграл {self.current_player}!")
            for row in self.button_grid:
                for btn in row:
                    btn.setEnabled(False)
        elif all(all(cell for cell in row) for row in self.board):
            self.game_active = False
            self.result.setText("Ничья!")
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.result.setText(f"Ход игрока {self.current_player}")

    def check_win(self):
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
                    all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        return all(self.board[i][i] == self.current_player for i in range(3)) or \
            all(self.board[i][2 - i] == self.current_player for i in range(3))

    def new_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for row in self.button_grid:
            for btn in row:
                btn.setText('')
                btn.setEnabled(True)
        self.game_active = True
        self.current_player = 'X' if self.x_radio.isChecked() else 'O'
        self.result.setText(f"Ход игрока {self.current_player}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())