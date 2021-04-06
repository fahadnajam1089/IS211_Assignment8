import random
import time

random.seed(0)

class Player():
    round = False

    def __init__(self, turn, name):
        self.name = name
        self.turn = turn
        self.score = 0
        self.round_score = 0

    def rolled(self):
        seed = random.randint(1, 6)
        return seed

    def hold_or_roll(self):
        while self.round != True:

            choose = input(self.name + "'s turn."+ " Your current score is "+str(self.score + self.round_score) +"\n" +"Enter 'r' to roll or 'h' to hold score: ")
            if choose == 'r':
                roll = self.rolled()
                print("You rolled a {}".format(roll))
                if roll == 1 :
                    print(self.name+" turn is over. \n")
                    self.round_score = 0
                    self.turn = False
                    self.round = True
                elif roll >= 2 and roll <= 6:
                    self.round_score += roll
                    print(self.name+" has {} points for this turn so far".format(self.round_score))
                if self.score + self.round_score >= 100:
                    self.score += self.round_score
                    print(self.name+" has won the Game!")
                    self.round = True
                    self.turn = False

            elif choose == 'h':
                self.score += self.round_score
                print(self.score)
                self.round_score = 0
                print(self.name + " has a TOTAL SCORE of {}.".format(self.score)+"\n")
                self.turn = False
                self.round = True

class ComputerPlayer(Player):
    def __init__(self, turn, name, t):
        super().__init__(turn,name)
        self.type = t

    def hold_or_roll(self):
        while self.round != True:
            if 25 < 100-self.score:
                lesser = 25
            else:
                lesser = 100-self.score 
            if self.round_score < lesser:
                choose = 'r'
            else:
                choose = 'h'
            if choose == 'r':
                roll = self.rolled()
                print("You rolled a {}".format(roll))
                if roll == 1 :
                    print(self.name+" turn is over. \n")
                    self.round_score = 0
                    self.turn = False
                    self.round = True
                elif roll >= 2 and roll <= 6:
                    self.round_score += roll
                    print(self.name+" has {} points for this turn so far".format(self.round_score))
                if self.score + self.round_score >= 100:
                    self.score += self.round_score
                    print(self.name+" has won the Game!")
                    self.round = True
                    self.turn = False

            elif choose == 'h':
                self.score += self.round_score
                print(self.score)
                self.round_score = 0
                print(self.name + " has a TOTAL SCORE of {}.".format(self.score)+"\n")
                self.turn = False
                self.round = True


class PlayerFactory(object):
    # Create based on class name:
    def factory(type,name):
        #return eval(type + "()")
        if type == "human": return Player(True, name)
        if type == "computer": return ComputerPlayer(False,"Computer","comp")
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)


class TimedGameProxy():
    def __init__(self):

        self.start_time = time.time()
        self.end_time = time.time()

    def game_timer(self):
        self.end_time = time.time()
        print(str(self.end_time - self.start_time)+" has passed ......")
        if self.end_time - self.start_time >= 60:
            return True
        else:
            return False
def main():
    player1 = input("Enter player1 type: 'human' or 'computer': ")

    # making player 1
    if player1 == "human":
        player1 = PlayerFactory.factory("human",input("Enter player's name: "))
    elif player1 == "computer":
        player1 = PlayerFactory.factory("computer","COMPUTER")

    # making player 2
    player2 = input("Enter player2 type: 'human' or 'computer': ")
    if player2 == "human":
        player2 = PlayerFactory.factory("human",input("Enter player's name: "))
    elif player2 == "computer":
        player2 = PlayerFactory.factory("computer","COMPUTER")

        
    timer = input("Set a 1 min. timer: 'yes' or 'no': ")
    if timer == 'yes':
        timed = TimedGameProxy()
        timed.game_timer()
    elif timer == 'no':
        pass
    
    gameOver = False
    while gameOver == False:
      
      if timer == 'yes':
          flag = timed.game_timer()
          if flag == True:
              print("*******TIME IS UP*******")
              if player1.score > player2.score:
                  print(player1.name+" Wins")
              elif player1.score < player2.score:
                  print(player2.name+" Wins")
              else:
                  print("It is a draw")
              break
      if player1.turn == True:
        player1.hold_or_roll()
        if player1.score >= 100:
          gameOver = True
        player2.turn = True
        player1.round = False
      else:
        player2.hold_or_roll()
        if player2.score >= 100:
          gameOver = True
        player1.turn = True
        player2.round = False


if __name__ == "__main__":
    main()
