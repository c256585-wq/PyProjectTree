class FileManager:

    def load_file(self, filename):
        """
        Считывает данные из файла и выполняет проверку
        корректности входных данных перед построением дерева.
        """
        data = []

        try:
            with open(filename, "r", encoding="utf-8") as file:

                for line in file:
                    line = line.strip()

                    if line == "":
                        continue

                    parts = line.split()

                    if len(parts) != 2:
                        raise Exception("\n>>> В каждой строке должно быть по 2 значения!")


                    try:
                        value = int(parts[0])
                    except ValueError:
                        raise Exception("\n>>> Значения в дереве должны быть целыми числами!")


                    code = parts[1]

                    for symbol in code:

                        if symbol not in ("0", "1"):
                            raise Exception("\n>>> Код должен содержать только 0 и 1.")

                    data.append((value, code))

        except FileNotFoundError:
            raise FileNotFoundError("\n>>> Файл не найден")
        if len(data) == 0:
            raise Exception("\n>>> Файл не содержит данных")

        codes = []
        """
        Каждый код добавляется в список codes,
        а при повторном обнаружении считается ошибкой.
        """
        for value, code in data:
            if code in codes:
                raise Exception("\n>>> Коды не должны повторяться!")
            codes.append(code)

        return data
