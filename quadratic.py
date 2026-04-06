# Replace the "ANSWER HERE" for your answer
import math

def roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return '( )'
    root1 = (-b + (discriminant ** 0.5)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return f'({root1})'
    else:
        return f'({root1}, {root2})'


def value_y(a, b, c, x):
    y = a * (x ** 2) + b * x + c
    return y


def to_string(a, b, c):
    answer = 'f(x) = '
    if a != 0:
        answer += f"{a} * X^2"
    if b != 0:
        if a != 0:
            answer += " + "
        answer += f"{b} * X"
    if c != 0:
        if b != 0 or a != 0:
            answer += " + "
        answer += f"{c}"
    return answer


def derivation(a, b, c):
    answer = """f'(x) = """
    if a != 0:
        answer += f"{a*2} * X"
        if b != 0:
            answer += " + "
    if b != 0:
        answer += f"{b}"
    if a == 0 and b == 0:
        answer += "0"
    return answer
