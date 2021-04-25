import random

class Computer:
    penalty = 2 # The user has 5 changes to guess the number correctly
    winP = 4 # The user wins 2 more changes to continue playing
    #hints = 1 # how many hints the player has. It's a future feature
    start = 0 # The start of the range
    stop = 10 # The end of the range

    def __init__(self):
        """
        @description: This method just initializes the private instance variable __number.
         The value -1 indicates that the computer has not picked a number yet
        """
        self.__number = -1

    def pickANumber(self):
        """
        @description: 
         - This method is used by the computer to pick a random integer number with the help of "randint" function
         - Then this number is assigned to the private instance variable __number
        """
        num = random.randint(self.start,self.stop)
        self.setComputerNumber(num)

    def didUserPickedTheRightNumber(self,num):
        """
        :param num: This method accepts a parameter named num which is the number that the user picked
        :return: The method returns True if the user guessed the number corrently, otherwise it returns False
        @description:
         - This function just compares the number that the user picked with the value that the computer randomly chose
        """
        if(num == self.getComputerNumber()):
            return True
        return False

    def checkUserNumber(self, userObject):
        """
        :param userObject: This parameter is an instance of the User class
        @description: 
         - This method checks if the user guessed corrently or not with the help of "didUserPickedTheRightNumber" method
         - If the user guessed corrently then the user wins "winP" points, otherwise the user lossed "penalty" points
        """
        if(self.didUserPickedTheRightNumber(userObject.getUserNumber())):
            print("[*] You have guessed correctly\n\t[>] You won {} points".format(self.winP))
            userObject.atomicPointsWin(self.winP)
            self.pickANumber()
        else:
            print("[*] You have guessed incorrectly\n\t[>] You lost {} points".format(self.penalty))
            userObject.atomicPointsPenalty(self.penalty)

    def setComputerNumber(self,number):
        """
        :param number: This parameter is used to set the private variable __number
        """
        self.__number = number

    def getComputerNumber(self):
        """
        @description:
         - This method is used to retrieve the value of the private instance variable __number
        """
        return self.__number