def isPalindrome(self, x):
        str_x = str(x)
        for i in range(len(str_x)):
            if str_x[i] != str_x[len(str_x)-1-i]:
                return False
        return True
