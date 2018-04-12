"""
    Introduction to Programming
    Scoring for Molkky
"""


# TODO: Implement the class Player here

class Player:

    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__turn = 0
        self.__score = 0
        self.__failTurn = 0
        self.__hit_percentage = 0


    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points


    def has_won(self):
        if self.__points == 50:
            return True
        else:
            return False


    def add_points(self, pts):
        self.__points += pts
        self.__score += pts
        self.__turn += 1
        if pts == 0:
            self.__failTurn += 1
        if pts > self.__score / self.__turn:
            print("Cheers " + self.__name + "!")
        if self.__points > 50:
            print(self.__name + " gets penalty points!")
            self.__points = 25
        if 40 <= self.__points <= 49:
            print(self.__name + " needs only " + str(50 - self.__points) + " points. It's better to avoid knocking down the pins with higher points.")

    def hit_percentage(self):
        if self.__turn == 0:
            return 0.0
        else:
            self.__hit_percentage = float((self.__turn - self.__failTurn) * 100 /(self.__turn))
            return self.__hit_percentage

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
        in_turn.hit_percentage()
        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ": " + str(player1.get_points()) + " p" + ", hit percentage  " + "%.1f" % player1.hit_percentage())
        print(player2.get_name() + ": " + str(player2.get_points()) + " p" + ", hit percentage " + "%.1f" % player2.hit_percentage())
        print("")

        throw += 1

main()

