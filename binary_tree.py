from node import Node

class BinaryTree:

    def __init__(self):
        self.root = Node(0)

    def insert(self, value, code):
        """
        Добавляет узел в дерево по заданному коду пути.
        current - корень
        0 - переход к левому потомку, 1 - к правому.
        Если необходимый промежуточный узел отсутствует,
        он создаётся автоматически (None).
        Потом в конечный узел записывается значение.
        """
        current = self.root

        for symbol in code:
            if symbol == "0":
                if current.left is None:
                    current.left = Node()
                current = current.left

            elif symbol == "1":
                if current.right is None:
                    current.right = Node()
                current = current.right

        current.value = value

    def build_tree(self, data):

        for value, code in data:
            self.insert(value, code)

    def print_tree(self, node, level=0):
        """
        Выводит дерево в повёрнутом виде.

        Для отображения структуры сначала
        рекурсивно выводится правое поддерево,
        потом текущий узел и затем левое поддерево.
        Параметр level определяет величину
        отступа и соответствует глубине узла в дереве.
        """
        if node is not None:
            self.print_tree(node.right, level + 1)
            print("    " * level + str(node.value))
            self.print_tree(node.left, level + 1)

    def count_nodes(self):
        return self.count(self.root)

    def count(self, node):
        """
        Рекурсивно подсчитывает количество узлов дерева.

        Для существующего узла учитывается он сам (+1)
        и количество узлов в левом и правом поддеревьях.
        """
        if node is None:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)

    def height(self):
        return self.get_height(self.root)

    def get_height(self, node):
        """
        Рекурсивно вычисляет высоту поддерева.

        Высота определяется как максимальная высота
        левого и правого поддеревьев + 1 уровень
        для текущего узла.
        """
        if node is None:
            return 0
        return max(
            self.get_height(node.left),
            self.get_height(node.right)
        ) + 1
