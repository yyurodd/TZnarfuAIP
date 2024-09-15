from PyQt5.QtWidgets import QWidget, QApplication


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
        self.root = None

    def getRoot(self):
        '''
        Получение значения корня
        '''
        return self.root

    def add(self, val: int) -> None:
        '''
        Добавление узла.
        Если дерево не содержит элементов, создаем дерево из одного элемента.
        Если дерево не пустое, вызываем вспомогательную функцию добавления.
        '''
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val: int, node: Node) -> None:
        '''
        Вспомогательная рекурсивная функция добавления.
        Если элемент меньше значения текущего узла,
        добавляем его в левое поддерево.
        В противном случае добавляем его в правое поддерево.
        '''
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val: int):
        '''
        Поиск узла.
        Если узел не пуст, вызываем вспомогательную функцию поиска,
        иначе возвращаем None.
        '''
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val: int, node: Node):
        '''
        Вспомогательная рекурсивная функция поиска.
        Если узел найден, возвращаем его. Если значение узла больше искомого,
        продолжаем поиск в левом поддереве, если оно не пустое. Если значение
        узла меньше искомого, продолжаем поиск в правом поддереве,
        если оно не пустое.
        '''
        if val == node.v:
            return node.v
        elif (val < node.v and node.l != None):
            return self._find(val, node.l)
        elif (val > node.v and node.r != None):
            return self._find(val, node.r)

    def deleteTree(self):
        '''
        Удаление дерева.
        '''
        self.root = None

    def nodesCounter(self,node:Node):
        if node is None:
            return 0
        return 1 + self.countNodes(node.l) + self.countNodes(node.r)

    def leafCounter(self, node):
        if node is None:
            return 0
        if node.l is None and node.r is None:
            return 1
        return self.leaf_counter(node.l) + self.leaf_counter(node.r)

    def treeHeight(self, node):
        if node is None:
            return 0
        else:
            l_height = self.tree_height(node.l)
            r_height = self.tree_height(node.r)
            return max(l_height, r_height) + 1


if __name__ == "__main__":
    tree = BinarySearchTree()


