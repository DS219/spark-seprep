def fizz_buzz(n):
        """
        :type n: int
        :rtype: List[str]
        """
        i = 1
        sol = []
        while(i < n + 1):

            if(i % 3 == 0 and i % 5 == 0):
                sol.append("FizzBuzz")
            elif(i % 3 == 0):
                sol.append("Fizz")
            
            elif(i % 5 == 0):
                sol.append("Buzz")

            else:
                sol.append(str(i))

            i+=1

        return sol

# Test case
result = fizz_buzz(3)
print(result)