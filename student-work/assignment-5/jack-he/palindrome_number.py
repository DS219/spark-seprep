class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        reverse = 0
        num = x

        while num != 0:
            # Adds each place value from num to reverse backwards
            reverse = reverse * 10 + num % 10
            num = num // 10

        return reverse == x

# Create an instance of Solution
solution = Solution()

#Test case 1: Num is Palindrome - Returns true
num1 = 131
print(f"The number {num1} is a Palindrome: {solution.isPalindrome(num1)}")

#Test case 2: Num is Not a Palindrome (ends in 0) - Returns false
num2 = 1310
print(f"The number {num2} is a Palindrome: {solution.isPalindrome(num2)}")

#Test case 3: Num is Not a Palindrome (is negative) - Returns false
num3 = -454
print(f"The number {num3} is a Palindrome: {solution.isPalindrome(num3)}")

#Test case 4: Num is Not a Palindrome - Returns false
num4 = 123
print(f"The number {num4} is a Palindrome: {solution.isPalindrome(num4)}")