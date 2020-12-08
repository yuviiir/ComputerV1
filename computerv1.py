import sys
import re

def main():
    equation = simplify_equation(sys.argv[1].upper())
    print("Reduced form: " + equation + " = 0")
    degree = polynomial_degree(equation)
    print("Polynomial degree: " + str(degree))

def simplify_equation(equation):
    left = equation.split(" = ")[0]
    right = equation.split(" = ")[1]
    equation_split = right.split(" ")
    if (equation_split[0] == "-"):
        equation_split.pop(0)
        equation_split.insert(0, "+")
    else:
        equation_split.insert(0, "-")
    i = 1
    while (i < len(equation_split)):
        if (equation_split[i] == "+"):
            equation_split[i] = "-"
        elif (equation_split[i] == "-"):
            equation_split[i] = "+"
        i += 1 
    changed_equation = left + " " + " ".join(equation_split)
    equation_split = changed_equation.split(" ")
    if (equation_split[0] != "-"):
        equation_split.insert(0, "+")
    i = 3
    j = i + 4
    while (i < len(equation_split)):
        while (j < len(equation_split)):
            if (equation_split[i] == equation_split[j]):
                sum = int(equation_split[i - 2]) if equation_split[i - 3] == "+" else int(equation_split[i - 2]) * -1
                sum = sum + int(equation_split[j - 2]) if equation_split[j - 3] == "+" else sum - int(equation_split[j - 2])
                if (sum < 0):
                    equation_split[i - 3] = "-"
                    equation_split[i - 2] = str(sum * -1)
                else:
                    equation_split[i - 3] = "+"
                    equation_split[i - 2] = str(sum)
                equation_split.pop(j)
                equation_split.pop(j - 1)
                equation_split.pop(j - 2)
                equation_split.pop(j - 3)
                j -= 4
            j += 4
        i += 4
        j = i + 4
    if (equation_split[0] != "-"):
        equation_split.pop(0)
    simplified_equation = " ".join(equation_split)
    return (simplified_equation)

def polynomial_degree(equation):
    equation_split = equation.split(" ")
    i = 0
    highest_degree = 0

    while (i < len(equation_split)):
        if ("X" in equation_split[i]):
            degree = int(equation_split[i][len(equation_split[i]) - 1])
            highest_degree = degree if degree > highest_degree else highest_degree
        i += 1
    return (highest_degree)

main()