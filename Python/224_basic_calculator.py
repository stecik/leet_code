import re


def calculate(s: str) -> int:
    s = s.replace(" ", "")
    s = "(" + s
    s = s[::-1]
    stack = []
    stack.append(")")
    for char in s:
        if char == "(":
            expression = ""
            while not stack[-1] == ")":
                expression += stack.pop(-1)
            stack.pop(-1)
            print(expression)
            stack.extend(evaluate(expression))
            print(stack)
        else:
            stack.append(char)
    return int("".join(stack[::-1]))


def evaluate(expression: str) -> list:
    expression = expression.replace("+-", "-")
    expression = expression.replace("--", "+")
    stack = re.split(r"([+-])", expression)[::-1]
    stack = [char for char in stack if char != ""]
    print(stack)
    while len(stack) > 2:
        if stack[-1] == "-" or stack[-1] == "+":
            stack.append("0")
        a = int(stack.pop(-1))
        sign = stack.pop(-1)
        b = int(stack.pop(-1))
        print(a, sign, b)
        if sign == "+":
            stack.append(str(a + b))
        elif sign == "-":
            stack.append(str(a - b))
        print(stack)
    return stack


s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s))
print(eval(s))
print()
s = "((33 + 2) - (1 + 5)) + (8 - (4 + 2 + 3))"
print(calculate(s))
print(eval(s))
print()
s = "1-(     -2)"
print(calculate(s))
print(eval(s))
s = "-2+ 1"
print(calculate(s))
print(eval(s))
print()
s = "- (3 + (4 + 5))"
print(calculate(s))
print(eval(s))
print()
s = "-(-2)+4"
print(calculate(s))
print(eval(s))
print()
