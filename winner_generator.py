#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout 
from random import randint
#создание элементов интерфейса
def show_boom():
    if number.text() == '?':
        random_number = randint(1, 195)
        number.setText(str(random_number))
        text.setText('Ядерка отправлена')
        btn.setText('Тикай нафиг')
    elif btn.text() == 'Тикай нафиг':
        window.close()
app = QApplication([])
window = QWidget()

#привязка элементов к вертикальной линии
window.setWindowTitle('Атомайзер')
window.resize(1000, 900)
window.move(54, 25)
#обработка событий
text = QLabel('Нажми и не задавай вопросов!')
number = QLabel('?')
btn = QPushButton('Нажми на меня')
btn.clicked.connect(show_boom)
v_LIne = QVBoxLayout()
v_LIne.addWidget(text, alignment = Qt.AlignCenter)
v_LIne.addWidget(number, alignment = Qt.AlignCenter)
v_LIne.addWidget(btn, alignment = Qt.AlignCenter)
window.setLayout(v_LIne)

#запуск приложения
window.show()
app.exec()