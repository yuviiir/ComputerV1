import sys
import re

def main() :
    if len(sys.argv) == 2 :
        equation = simplify_equation(sys.argv[1].upper())
        print("Reduced form: " + equation + " = 0")

def simplify_equation(equation) :
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
    print(changed_equation)
    equation_split = changed_equation.split(" ")
    if (equation_split[0] != "-"):
        equation_split.insert(0, "+")
    i = 3
    j = i + 4
    while (i < len(equation_split)):
        while (j < len(equation_split)):
            if (equation_split[i] == equation_split[j]):
                if (equation_split[i - 3] == "+"):
                    sum = int(equation_split[i - 2])
                else:
                    sum = int(equation_split[i - 2]) * -1
                if (equation_split[j - 3] == "+"):
                    sum = sum + int(equation_split[j - 2])
                else:
                    sum = sum - int(equation_split[j - 2])
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

main()