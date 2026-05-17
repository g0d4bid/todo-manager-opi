import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QLabel, QLineEdit, QPushButton, QListWidget,
                             QMessageBox)

class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Записная книжка')
        self.setGeometry(300, 300, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        layout.addWidget(QLabel("Имя"))
        self.contactName = QLineEdit()
        layout.addWidget(self.contactName)

        layout.addWidget(QLabel("Телефон"))
        self.contactNumber = QLineEdit()
        layout.addWidget(self.contactNumber)

        self.addContactBtn = QPushButton("Добавить")
        self.addContactBtn.clicked.connect(self.add_contact)
        layout.addWidget(self.addContactBtn)

        layout.addWidget(QLabel("Список контактов:"))
        self.contactList = QListWidget()
        layout.addWidget(self.contactList)

    def add_contact(self):
        name = self.contactName.text().strip()
        phone = self.contactNumber.text().strip()

        if not name or not phone:
            QMessageBox.warning(self, "Ошибка", "Надо заполнить оба поля")
            return

        self.contactList.addItem(f"{name}: {phone}")
        self.contactName.clear()
        self.contactNumber.clear()
        self.contactName.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyNotes()
    window.show()
    sys.exit(app.exec_())