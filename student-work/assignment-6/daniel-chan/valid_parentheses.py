def isValid(s):
        #initialize the stack
        stackOfParan = []
        #for every ) there must be a ( for it to be valid. same pattern emerges for square brackets and curly
        validParenthesis = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in validParenthesis:
                #if c is one of the keys in the validParenthesis dictionary then you want to check if there is a corresponding value. but you can't check if the stack is empty
                if len(stackOfParan)> 0 and stackOfParan[-1] == validParenthesis[c]:
                    #pop if it is the corresponding value, else we know its false
                    stackOfParan.pop()
                else:
                    return False
            else:
                #always append the open bracket
                stackOfParan.append(c)
        #if nothing is in the stack it just means everything was valid
        return len(stackOfParan)==0

#test code:
string1 = "([])"
string2 = "()[]{}"
string3 = "([)]"
result1 = isValid(string1)
result2 = isValid(string2)
result3 = isValid(string3)
print(str(result1) + " is the result of " + string1 + " when figuring out if it is a valid set of parentheses or not")
print(str(result2) + " is the result of " + string2 + " when figuring out if it is a valid set of parentheses or not")
print(str(result3) + " is the result of " + string3 + " when figuring out if it is a valid set of parentheses or not")
#1 and 2 are true because every bracket is closed by the correct corresponding one
#3 is false because [) don't match 


