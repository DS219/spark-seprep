   


#Adds the num until it becomes a single digit 
# 38 = 3 + 8 -> 11
# 11 = 1 + 1 -> 2
# return 2
def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9

    testcase = 38
    print("This is the result: ", addDigits(testcase))


        
