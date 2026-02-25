def isValid(self, s: str) -> bool:
        starting_bracket = []
        popped_value = None
        

        for i in range(len(s)):
            if len(starting_bracket) == 0 and (s[i] == ')' or s[i] == ']' or s[i] == "}"):
                return False
            if s[i] == '(' or s[i] == '[' or s[i] == "{":
                starting_bracket.append(s[i])
                continue
            if s[i] == ')':
                popped_value = starting_bracket.pop()
                if popped_value != '(':
                    return False
                else:
                    continue
            elif s[i] == ']':
                popped_value = starting_bracket.pop()
                if popped_value != '[':
                    return False
                else:
                    continue
            elif s[i] == '}':
                popped_value = starting_bracket.pop()
                if popped_value != '{':
                    return False
                else:
                    continue

        if len(starting_bracket) != 0:
            return False 
        return True

            
