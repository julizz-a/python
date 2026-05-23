import os
class Player:
    def __init__(self, number):
        self.number = number
        self.name = f"Игрок {number}"
        self.score = 0
        self.choice = ""

    def make_choice(self):
        print(f"\n{self.name}, твой ход")
        choice = input("камень, ножницы или бумага? ").lower()
        while choice not in ["камень", "ножницы", "бумага"]:
            choice = input("ошибка при вводе, попробуй ещё раз: ").lower()
        self.choice = choice
        return choice

    def add_point(self):
        self.score += 1

    def get_score(self):
        return self.score

    def get_choice(self):
        return self.choice

    def get_name(self):
        return self.name


class Comparison:
    def __init__(self, players):
        self.players = players

    def get_winners(self):
        choices = [player.get_choice() for player in self.players]

        if len(set(choices)) == 1:
            return None

        winners = []
        for i, player in enumerate(self.players):
            player_choice = player.get_choice()
            is_winner = True
            for j, other_player in enumerate(self.players):
                if i != j:
                    other_choice = other_player.get_choice()
                    if (player_choice == "камень" and other_choice == "бумага") or \
                            (player_choice == "ножницы" and other_choice == "камень") or \
                            (player_choice == "бумага" and other_choice == "ножницы"):
                        is_winner = False
                        break

            if is_winner:
                winners.append(player)

        return winners if winners else None


class Display:
    def __init__(self, players):
        self.players = players

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_score(self):
        print(f"\nТекущий счёт:")
        for player in self.players:
            print(f"{player.get_name()}: {player.get_score()} очков")

    def show_winners(self, winners):
        if winners is None:
            print("\nНичья, никто не получает очко")
        elif len(winners) == 1:
            print(f"\n{winners[0].get_name()} победил в раунде")
        else:
            print("\nНичья между несколькими игроками!")

    def add_points_to_winners(self, winners):
        if winners is not None:
            for winner in winners:
                winner.add_point()

    def show_final_result(self):
        print("итоговые результаты")
        for player in self.players:
            print(f"{player.get_name()}: {player.get_score()} очков")

        max_score = max(player.get_score() for player in self.players)
        winners = [player for player in self.players if player.get_score() == max_score]

        if len(winners) == 1:
            print(f"\n{winners[0].get_name()} победил в игре!")
        else:
            print("\nНичья в игре!")


class Game:
    def __init__(self):
        self.players = []
        self.num_players = 0
        self.num_rounds = 0
        self.comparison = None
        self.display = None

    def setup(self):
        print("настройка игры")

        while True:
            try:
                self.num_players = int(input("Сколько игроков? (2-5): "))
                if 2 <= self.num_players <= 5:
                    break
                else:
                    print("Введите число от 2 до 5")
            except ValueError:
                print("Введите число")

        for i in range(self.num_players):
            self.players.append(Player(i + 1))

        while True:
            try:
                self.num_rounds = int(input("Сколько будет раундов? (1-20): "))
                if 1 <= self.num_rounds <= 20:
                    break
                else:
                    print("Введите число от 1 до 20")
            except ValueError:
                print("Введите число")

        self.comparison = Comparison(self.players)
        self.display = Display(self.players)

    def play_round(self, round_number):
        print(f"раунд {round_number} из {self.num_rounds}")
        for i, player in enumerate(self.players):
            self.display.clear_screen()
            print(f"РАУНД {round_number} из {self.num_rounds}")
            self.display.show_score()
            player.make_choice()
            print("\n" * 30)
            if i < len(self.players) - 1:
                input("Нажмите Enter для следующего игрока...")
        self.display.clear_screen()

        print(f"раунд {round_number} из {self.num_rounds} - результаты")

        winners = self.comparison.get_winners()
        self.display.show_winners(winners)
        self.display.add_points_to_winners(winners)
        self.display.show_score()

        if round_number < self.num_rounds:
            input("\nНажмите Enter для следующего раунда...")

    def start(self):
        self.setup()

        for round_num in range(1, self.num_rounds + 1):
            self.play_round(round_num)

        self.display.show_final_result()

game = Game()
game.start()