    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

#test case
digits = [9, 9, 9]
target= [1,0,0,0]
result = plusOne(digits)
print(f"Digits after adding one should be: {target} : {result}")
