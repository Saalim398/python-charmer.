#valid parenthesis.py

string = "[{((()}]"

def isValid(s):
    valid = []
    pairs = {')':'(', '}':'{', ']':'['}

    for par in s:
        if par in "({[":
            valid.append(par)
        elif par in ")}]":
            if not valid or valid[-1] != pairs[par]:
                return False
            valid.pop()
    return len(valid) == 0

print(isValid(string))
