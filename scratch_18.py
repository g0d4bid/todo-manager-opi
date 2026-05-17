import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QCheckBox, QPushButton, QPlainTextEdit)
class MacOrder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заказ в маке')
        self.setGeometry(300, 300, 400, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.menu_checkboxes = []
        menu_items = ["Чизбургер", "Гамбургер", "Кока-кола", "Наггетсы"]

        for item in menu_items:
            checkbox = QCheckBox(item)
            self.menu_checkboxes.append(checkbox)
            layout.addWidget(checkbox)

        self.order_btn = QPushButton("Заказать")
        self.order_btn.clicked.connect(self.make_order)
        layout.addWidget(self.order_btn)

        self.result = QPlainTextEdit()
        self.result.setReadOnly(True)
        self.result.setPlainText("Ваш заказ:\n")
        layout.addWidget(self.result)

    def make_order(self):
        selected_items = [cb.text() for cb in self.menu_checkboxes if cb.isChecked()]

        if selected_items:
            order_text = "Ваш заказ:\n\n" + "\n".join(f"- {item}" for item in selected_items)
        else:
            order_text = "Ваш заказ:\n\nНичего не выбрано"

        self.result.setPlainText(order_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MacOrder()
    window.show()
    sys.exit(app.exec_())