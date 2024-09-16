from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QBrush, QPen, QColor, QKeyEvent, QInputEvent

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, \
    QGraphicsTextItem, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
import sys

class Node:
    """
    Класс для хранения единичного узла бинарного дерева
    """

    def __init__(self, val):
        self.l = None  # Связь с левым потомком
        self.r = None  # Связь с правым потомком
        self.v = val  # Ключ (значение, которое хранится в узле)


class BinarySearchTree(QWidget):
    """
    Класс для хранения и графического отображения бинарного дерева поиска
    """

    def __init__(self):
        '''
        Конструктор
        '''
        super().__init__()
        self.setWindowIcon(QIcon("BT.ico"))
        self.initUI()
        self.root = None

    def initUI(self):
        self.resize(1000,800)
        self.setWindowTitle("Binary Search Tree")


        #основной вертикальный макет
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        #горизонтальный макет для поля ввода и кнопок
        inputLayout = QHBoxLayout()

        #поле ввода
        self.inputField = QLineEdit()
        self.inputField.setPlaceholderText("Введите значение узла...")
        inputLayout.addWidget(self.inputField)
        self.inputField.setStyleSheet('''
            QLineEdit {
                background-color: #FFFACD;
                color: black;
                border-radius: 10px;
                padding: 5px 10px;
            }
        ''')

        #кнопка добавления узла
        self.addButton = QPushButton("Добавить узел")
        self.addButton.clicked.connect(self.addNode)
        inputLayout.addWidget(self.addButton)
        self.addButton.setStyleSheet('''
                    QPushButton {
                        background-color: #FFFACD;
                        color: black;
                        border-radius: 10px;
                        padding: 5px 10px;
                    }

                    QPushButton:hover {
                        background-color: #2980b9;
                    }

                    QPushButton:pressed {
                        background-color: #1f618d;
                    }
                ''')

        # Кнопка очистки
        self.addButtonDel = QPushButton('Очистить')
        self.addButtonDel.clicked.connect(self.deleteTree)
        inputLayout.addWidget(self.addButtonDel)
        self.addButtonDel.setStyleSheet('''
                    QPushButton {
                        background-color: #FFFACD;
                        color: black;
                        border-radius: 10px;
                        padding: 5px 10px;
                    }

                    QPushButton:hover {
                        background-color: #2980b9;
                    }

                    QPushButton:pressed {
                        background-color: #1f618d;
                    }
                ''')

        # Кнопка нахождения высоты
        self.addButtonHeight = QPushButton('Высота')
        self.addButtonHeight.clicked.connect(self.treeHeight)
        inputLayout.addWidget(self.addButtonHeight)
        self.addButtonHeight.setStyleSheet('''
                    QPushButton {
                        background-color: #FFFACD;
                        color: black;
                        border-radius: 10px;
                        padding: 5px 10px;
                    }

                    QPushButton:hover {
                        background-color: #2980b9;
                    }

                    QPushButton:pressed {
                        background-color: #1f618d;
                    }
                ''')

        # Кнопка подсчета узлов
        self.addButtonNodes = QPushButton('Количество узлов')
        self.addButtonNodes.clicked.connect(self.nodesCounter)
        inputLayout.addWidget(self.addButtonNodes)
        self.addButtonNodes.setStyleSheet('''
                    QPushButton {
                        background-color: #FFFACD;
                        color: black;
                        border-radius: 10px;
                        padding: 5px 10px;
                    }

                    QPushButton:hover {
                        background-color: #2980b9;
                    }

                    QPushButton:pressed {
                        background-color: #1f618d;
                    }
                ''')

        # Кнопка подсчета листьев
        self.addButtonLeaves = QPushButton('Количество листьев')
        self.addButtonLeaves.clicked.connect(self.leafCounter)
        inputLayout.addWidget(self.addButtonLeaves)
        self.addButtonLeaves.setStyleSheet('''
                    QPushButton {
                        background-color: #FFFACD;
                        color: black;
                        border-radius: 10px;
                        padding: 5px 10px;
                    }

                    QPushButton:hover {
                        background-color: #2980b9;
                    }

                    QPushButton:pressed {
                        background-color: #1f618d;
                    }
                ''')

        mainLayout.addLayout(inputLayout)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        mainLayout.addWidget(self.view)

    #вызов функции добавления узла по нажатию клавиши "Enter"
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.addNode()

    def getRoot(self):
        '''
        Получение значения корня
        '''
        return self.root

    def addNode(self):
        data = self.inputField.text()
        if data.isdigit():
            if self.find(int(data)) == None:
                self.add(int(data))
                self.inputField.clear()
            else:
                QMessageBox.warning(self, 'Ошибка', 'Элемент уже существует в дереве.')
                self.inputField.clear()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Значение должно быть числом!')
            self.inputField.clear()

    def deleteTree(self):
        self.root = None
        self.scene.clear()

    # Функция для вычисления высоты
    def treeHeight(self):
        QMessageBox.information(self, 'Высота дерева', 'Высота: ' + str(self.height(self.getRoot())))

    # Функция для подсчета узлов
    def nodesCounter(self):
        QMessageBox.information(self, 'Количество узлов дерева', 'Количество узлов: ' + str(self.countNodes(self.getRoot())))


    # Функция для нахождения листьев
    def leafCounter(self):
        QMessageBox.information(self, 'Количество листьев в дереве', 'Количество листьев: ' + str(self.countLeaves(self.getRoot())))

    # Получение значения корня
    def getRoot(self):
        return self.root

    # Нахождение узла
    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    # Вспомогательная рекурсивная функция
    def _find(self, val, node):
        if val == node.v:
            return node.v
        elif (val < node.v and node.l != None):
            return self._find(val, node.l)
        elif (val > node.v and node.r != None):
            return self._find(val, node.r)

    # Функция вычисления высоты
    def height(self, node):
        if node is None:
            return 0
        else:
            l_hight = self.height(node.l)
            r_hight = self.height(node.r)
            return max(l_hight, r_hight) + 1

    # Функция подсчета узлов
    def countNodes(self, node):
        if node is None:
            return 0
        return 1 + self.countNodes(node.l) + self.countNodes(node.r)

    # Функция подсчета листьев
    def countLeaves(self, node):
        if node is None:
            return 0
        if node.l is None and node.r is None:
            return 1
        return self.countLeaves(node.l) + self.countLeaves(node.r)

    # Добавление узла на сцену
    def add(self, val):
        if self.root is None:
            self.root = Node(val)
            self.drawNode(val, 200, 50)
        else:
            self._add(val, self.root, 200, 50, 300)

    # Вспомогательная рекурсивная функция
    def _add(self, val, node, x, y, step):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l, x - step, y + 50, step // 2)
            else:
                node.l = Node(val)
                self.scene.addLine(x - 25, y, x - step, y + 50)
                self.drawNode(val, x - step, y + 50)
        else:
            if node.r is not None:
                self._add(val, node.r, x + step, y + 50, step // 2)
            else:
                node.r = Node(val)
                self.scene.addLine(x + 25, y, x + step, y + 50)
                self.drawNode(val, x + step, y + 50)

    # Отрисовка узла
    def drawNode(self, val, x, y):
        item = QGraphicsEllipseItem(x - 25, y - 25, 50, 50)
        item.setBrush(QBrush(QColor('white')))
        item.setPen(QPen(QColor('#00BFFF'), 4))
        self.scene.addItem(item)
        text = QGraphicsTextItem(str(val))
        text.setPos(x - 12.5, y - 12.5)
        self.scene.addItem(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tree = BinarySearchTree()
    tree.setStyleSheet('''
                    background-color: #B0C4DE;
                    border-radius: 10px;
                    padding: 5px 10px;
            ''')
    tree.show()
    sys.exit(app.exec())