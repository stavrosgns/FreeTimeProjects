class Player:
    points = 10 # All players start with 10 points

    def __init__(self):
        """
        @description:
         - This is the number which the player will pick. If it is -1 then the player haven't picked a number yet
           The value of this variable is accessible only through the function "getUserNumber"

         - Every player, depending if she/he guessed correctly, losses or wins points. We would be a bad practice
           to change the class variable
        """
        self.__number = -1
        self.__atomicPoints = self.points

    def __checkIfTheNumberIsInsideTheRange(self,num,a,b):
        """
        :param num: This is the number that the user picked
        :param a: This is the start of the range
        :param b: This is the end of the range
        :return: None
        @description:
         - This function takes the number that the user picked and checks if that number is between the approved
           range denoted by the numbers a and b

         - If the user pick a number outside the range, we raise a custom exception which is being handled in the
           except block

         - In the except block, we just call the "guessTheNumber" method until the user pick a number between
           the range
        """
        try:
            if((num >=a) and (num <=b)):
                self.__number = num
            else:
                raise Exception("[!] Please select a number between {} and {}".format(a,b))
        except:
            self.guessTheNumber(a,b)


    def guessTheNumber(self,a,b):
        """
        :param a: This the start of the range
        :param b: This is the end of the range
        :return: None
        @example using mathematical notation: [a,b]
        @description:
         - This method asks the user to pick a number between the range and
         - With the help of the private method "__checkIfTheNumberIsInsideTheRange" checks if the user picked the
           right number
        """
        number = int(input("[>] Please pick a number between {} and {} -> ".format(a,b)))
        self.__checkIfTheNumberIsInsideTheRange(number,a,b)

    def getUserNumber(self):
        """
        :return: This function returns the private instance variable __number
        @description: This is the only way to get the private instance variable
        """
        return self.__number

    def atomicPointsPenalty(self, penalty):
        """
        :param penalty: If the user guess the computer's number incorrectly then she/he losses "penalty" points
        :return: None
        """
        self.__atomicPoints -= penalty

    def atomicPointsWin(self,winP):
        """
        :param winP: If the user guess the computer's number correctly the she/he wins "winP" points
        :return: None
        """
        self.__atomicPoints += winP

    def getAtomicPoints(self):
        return self.__atomicPoints