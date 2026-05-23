class Element:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class AlchemyGame:
    def __init__(self):
        self.elements = {}
        self.recipes = {}

        self.elements["Вода"] = Element("Вода")
        self.elements["Огонь"] = Element("Огонь")
        self.elements["Земля"] = Element("Земля")
        self.elements["Воздух"] = Element("Воздух")

        self._create_recipes()

    def _create_recipes(self):
        self._add_recipe("Вода", "Огонь", "Пар")
        self._add_recipe("Вода", "Земля", "Растение")
        self._add_recipe("Земля", "Огонь", "Лава")
        self._add_recipe("Воздух", "Воздух", "Ветер")
        self._add_recipe("Воздух", "Ветер", "Мороз")
        self._add_recipe("Вода", "Мороз", "Лед")
        self._add_recipe("Растение", "Растение", "Дерево")
        self._add_recipe("Растение", "Земля", "Трава")
        self._add_recipe("Вода", "Вода", "Озеро")
        self._add_recipe("Озеро", "Вода", "Река")
        self._add_recipe("Вода", "Воздух", "Облако")
        self._add_recipe("Облако", "Вода", "Дождь")
        self._add_recipe("Трава", "Дождь", "Гриб")
        self._add_recipe("Облако", "Облако", "Молния")
        self._add_recipe("Молния", "Молния", "Энергия")
        self._add_recipe("Вода", "Энергия", "Жизнь")
        self._add_recipe("Земля", "Жизнь", "Червь")
        self._add_recipe("Воздух", "Жизнь", "Птица")
        self._add_recipe("Птица", "Птица", "Яйцо")
        self._add_recipe("Птица", "Огонь", "Феникс")
        self._add_recipe("Камень", "Огонь", "Металл")
        self._add_recipe("Земля", "Камень", "Гора")
        self._add_recipe("Дождь", "Солнце", "Радуга")
        self._add_recipe("Песок", "Огонь", "Стекло")
        self._add_recipe("Стекло", "Время", "Песок")

    def _add_recipe(self, elem1_name, elem2_name, result_name):
        key = tuple(sorted([elem1_name, elem2_name]))
        self.recipes[key] = result_name

    def combine(self, name1, name2):
        if name1 not in self.elements:
            print(f"Ошибка: элемент '{name1}' ещё не открыт.")
            return None
        if name2 not in self.elements:
            print(f"Ошибка: элемент '{name2}' ещё не открыт.")
            return None
        if name1 == name2:
            key = tuple([name1, name2])
            if key in self.recipes:
                result_name = self.recipes[key]
                if result_name in self.elements:
                    print(f"этот элемент уже открыт: {result_name}.")
                    return result_name
                else:
                    self.elements[result_name] = Element(result_name)
                    print(f"открыт новый элемент: {result_name}")
                    return result_name
            else:
                print(f"смешивание {name1} с самим собой ничего не даёт.")
                return None

        key = tuple(sorted([name1, name2]))
        if key in self.recipes:
            result_name = self.recipes[key]
            if result_name in self.elements:
                print(f"этот элемент уже открыт {result_name}.")
                return result_name
            else:
                self.elements[result_name] = Element(result_name)
                print(f"открыт новый элемент: {result_name}")
                return result_name
        else:
            print(f"смешивание {name1} и {name2} ничего не даёт...")
            return None

    def show_elements(self):
        print("открытые элементы")
        for name in sorted(self.elements.keys()):
            print(f"  • {name}")
        print(f" всего открыто: {len(self.elements)} элементов.")
        print()

    def show_help(self):
        print("команды:")
        print("  • список - показать все открытые элементы")
        print("  • рецепты - показать все известные рецепты")
        print("  • помощь - показать это сообщение")
        print("  • выход - выйти из игры")
        print()
        print("Чтобы смешать элементы, введите два элемента через пробел")
        print(" Например: вода огонь")

    def show_recipes(self):
        print("известные рецепты")
        shown = set()
        for key in sorted(self.recipes.keys()):
            elem1 = key[0]
            elem2 = key[1]
            result = self.recipes[key]
            if elem1 in self.elements and elem2 in self.elements:
                if result not in shown:
                    print(f"  {elem1} + {elem2} = {result}")
                    shown.add(result)
        print()

    def play(self):
        print("Смешивайте элементы, чтобы создавать новые!")
        print()
        self.show_help()
        self.show_elements()

        while True:
            user_input = input("\n Введите команду или два элемента: ").strip().lower()

            if user_input == "выход":
                print("\nСпасибо за игру, пока пока")
                break
            elif user_input == "список":
                self.show_elements()
            elif user_input == "рецепты":
                self.show_recipes()
            elif user_input == "помощь":
                self.show_help()
            else:
                parts = user_input.split()
                if len(parts) == 2:
                    elem1 = parts[0].capitalize()
                    elem2 = parts[1].capitalize()
                    print()
                    self.combine(elem1, elem2)
                else:
                    print("Неверная команда! Введите 'помощь' для списка команд.")


if __name__ == "__main__":
    game = AlchemyGame()
    game.play()
