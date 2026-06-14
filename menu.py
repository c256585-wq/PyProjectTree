from binary_tree import BinaryTree
from file_manager import FileManager


class Menu:

    def __init__(self):
        self.data = []
        self.tree = None
        self.file_manager = FileManager()

    def run(self):

        print("\nПостроение бинарного дерева по заданным кодам путей из файла:")

        while True:
            print("\n===== МЕНЮ =====")
            print("1. Загрузить файл")
            print("2. Просмотреть данные")
            print("3. Построить дерево")
            print("4. Показать дерево")
            print("5. Количество узлов")
            print("6. Высота дерева")
            print("0. Выход")

            choice = input("\nВыберите пункт: ")

            if choice == "1":
                self.load_data()

            elif choice == "2":
                self.show_data()

            elif choice == "3":
                self.build_tree()

            elif choice == "4":
                self.show_tree()

            elif choice == "5":
                self.show_nodes()

            elif choice == "6":
                self.show_height()

            elif choice == "0":
                print("Работа программы завершена.")
                break

            else:
                print("\n>>> Неверный пункт меню.")

    def load_data(self):

        try:
            filename = input("Введите название файла или путь: ")

            self.data = self.file_manager.load_file(filename)

            print("Файл успешно загружен.")
            print("Количество записей:", len(self.data))

        except Exception as error:
            self.data = []

            print(error)
            print(">>> Файл не был загружен.")

    def show_data(self):

        if len(self.data) == 0:
            print("\n>>> Данные не загружены.")
            return

        print("\nСодержимое файла:\n")

        for value, code in self.data:
            print(str(value) + " -> " + code)

    def build_tree(self):

        if len(self.data) == 0:
            print("\n>>> Сначала загрузите файл.")
            return

        try:
            self.tree = BinaryTree()
            self.tree.build_tree(self.data)
            print("\nДерево успешно построено.")

        except Exception as error:
            self.tree = None
            print(error)

    def show_tree(self):

        if self.tree is None:
            print("\n>>> Дерево не построено.")
            return

        print("\n Дерево выведено слева направо:\n")
        self.tree.print_tree(self.tree.root)

    def show_nodes(self):

        if self.tree is None:
            print("\n>>> Дерево не построено.")
            return

        print("Количество узлов:", self.tree.count_nodes())

    def show_height(self):

        if self.tree is None:
            print("\n>>> Дерево не построено.")
            return

        print("Высота дерева:", self.tree.height())
