import formatting as f
import random as r

f.clear_console()

f.title("Mini Project 2: Classes")

f.dash()

f.section("Welcome to the Lottery!")


class Lottery:
    def __init__(self):
        """Makes a pool of letters and numbers to choose from and defines variables"""
        self.pool = ['1','2','3','4','5','6','7','8','9','10',"a","b","c","d","e"]
        self.winning_ticket = self.draw()


    def draw(self):
        """generates the 'winning combination' to determine if the user determined the right combination to win the lottery"""
        return r.sample(self.pool, 4)

    def get_user_ticket(self):
        lottery_guess = input("Input your four unique values for the lottery, seperated by a comma and space:\n").split(", ")
        return lottery_guess

    def analyze_ticket(self, user_ticket):
        counter = 0
        while True:
            counter += 1
            self.winning_ticket = self.draw()
            if set(self.winning_ticket) == set(user_ticket):
                return counter

lottery = Lottery()
user_guess = lottery.get_user_ticket()

f.dash()

f.section("Lottery Analysis")
        
print(f"It took {lottery.analyze_ticket(user_guess)} times for your guess to be the winning combination.")

f.dash()
