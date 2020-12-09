import sys

def main():
    equation = simplify_equation(sys.argv[1].upper())
    print("Reduced form: " + equation + " = 0")
    degree = polynomial_degree(equation)
    print("Polynomial degree: " + str(degree))
    if (degree > 2):
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    else:
        solve_equation(equation)

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

def solve_equation(equation) :
    highest_power = polynomial_degree(equation)
    equation_split = equation.split(" ")
    i = 0
    while (i < len(equation_split)):
        if (equation_split[i] == "X^0"):
            c = float(equation_split[i - 2]) if equation_split[0] != "-" else float(equation_split[i - 2]) * -1
        if (equation_split[i] == "X^1"):
            b = float(equation_split[i - 2]) if equation_split[i - 3] != "-" else float(equation_split[i - 2]) * -1
        if (equation_split[i] == "X^2"):
            a = float(equation_split[i - 2]) if equation_split[i - 3] != "-" else float(equation_split[i - 2]) * -1
        i += 1
    if highest_power == 0:
        if c == 0 :
            print ("The solution is all real numbers")
        else :
            print("No real solution")
    if highest_power == 1:
        solution = (c * -1) / (b)
        print("Solution: " + str(solution))
    if highest_power == 2:
        if a == 0:
            print("Can't solve!")
            return(0)
        if (b**2 - (4*a*c)) < 0:
            print("Discriminant is strictly negative, the two solutions are:")
            solution = (-b - (b**2 - (4*a*c))**0.5)/(2 * a)
            print(str(solution))
            solution = (-b + (b**2 - (4*a*c))**0.5)/(2 * a)
            print(str(solution))
            return(0)
        print("Discriminant is strictly positive, the two solutions are:")
        solution = (-b - (b**2 - (4*a*c))**0.5)/(2 * a)
        print(str(solution))
        solution = (-b + (b**2 - (4*a*c))**0.5)/(2 * a)
        print(str(solution))

main()