import Player
import Computer

if(__name__ == "__main__"):
    # |STAGE 1: Create The Players and Let The Computer Pick a Number |
    computer = Computer.Computer()
    computer.pickANumber()
    start = computer.start
    stop = computer.stop
    
    user = Player.Player()


    # |STAGE 2: Let The User Pick a Number |
    while(user.getAtomicPoints() >= 0):
        user.guessTheNumber(start, stop)

        # |STAGE 3: Check If The User Guessed Correctly |
        computer.checkUserNumber(user)
        print("[*] You have {} / 10 points".format(user.getAtomicPoints()))
    else:
        print("[ :( ] Game Over")