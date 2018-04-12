"""
TIE-02106 Introduction to programming
Mölkky
"""


class Player:
    def __init__(self, name):
        self.__score = 0
        self.__name = name
        self.__throws = 0
        self.__success = 0
        self.__totalPoints = 0


    def get_name(self):
        return self.__name

    def add_points(self, score):
        new_score = self.__score + score
        self.__throws = self.__throws + 1
        self.__totalPoints += score
        if score > 0:
            self.__success += 1
        if new_score > 50:
            print(self.__name + " gets penalty points!")
            self.__score = 25
        elif new_score <= 50:
            self.__score = new_score
            if 40 <= self.__score <= 49:
                score_needed = 50 - self.__score
                print(self.__name, "needs only", score_needed,
                      "points. It's better to "
                      "avoid knocking down the pins with higher points.")
        average_score = self.__totalPoints / self.__throws
        if score > average_score:
            print("Cheers", self.__name + "!")

    def has_won(self):
        if self.__score == 50:
            return True

    def get_points(self):
        return self.__score

    def get_percent(self):
        if self.__throws == 0:
            return 0.0
        else:
            return float(self.__success * 100 / self.__throws)


def main():

    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!
    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        if throw % 2 == 0:
            in_turn = player1
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))
        in_turn.add_points(pts)
        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p, hit percentage",
              player1.get_percent())
        print(player2.get_name() + ":", player2.get_points(), "p, hit percentage",
              player2.get_percent())
        print("")

        throw += 1


main()
