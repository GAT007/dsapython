#Balanced Parentheses Check
#Given a string of opening and closing parentheses, check whether it's balanced. We have 3 types of parentheses: round brackets ()
#Square brackets [] and curly brackets {}

def balance_check(s):
    #Edge case check
    if len(s)%2 != 0:
        return False
    items = []
    for bracket in s:
        if bracket in ('[', '{', '('):
            items.append(bracket)
        else:
            if len(items) == 0:
                return False
            if bracket == ']' and items[-1]!= '[':
                return False
            elif bracket == '}' and items[-1]!= '{':
                return False
            elif bracket == ')' and items[-1]!= '(':
                return False
            else:
                items.pop()

    return True


print(balance_check('[()]}{'))

