

# function af addition (+)
def add(varOne,varTwo):
    sum = varOne + varTwo
    return sum

#function of subtraction (-)
def subtract(varOne,varTwo):
    subtraction = varOne - varTwo
    return subtraction

#function of mutiplication (*)
def multiplication(varOne,varTwo):
    multiply = varOne * varTwo
    return multiply

#function of division (/)
def division(varOne,varTwo):
    divide = varOne/varTwo
    return divide

#importing math library
import math

#function of power (^)
def power(varOne,varTwo):
    powerIs = math.pow(varOne,varTwo)
    return powerIs

#function of log to some base (log)
def logrithm(varOne,varTwo):
    logIs = math.log(varOne,varTwo)
    return logIs

#function for log to base "e" (ln)
def logrithmBaseE(varOne):
    logOne = math.ln(varOne)
    return logOne

#function of nth-root. varOne raise to the power 1/varTwo (1/n)
def root(varOne,varTwo):
    answer = math.pow(varOne,1/varTwo)
    return answer

#function of average (avg)
def average(varOne,varTwo):
    avg = (varOne+varTwo)/2
    return avg

#function of factorial (!)
def factorial(varOne):
    firstFactorial = math.factorial(varOne)
    return firstFactorial

#function for gcd (gcd)
def gcd(a,b):
    greatestCommonDivisor = math.gcd(a,b)
    return greatestCommonDivisor

#function of sin (sin)
def sin(var):
    return (math.sin(var))

#function of cos (cos)
def cos(var):
    return  (math.cos(var))

#function of tan (tan)
def tan(var):
    return (math.tan(var))

#function of sin inverse (asin)
def sinInversse(var):
    return (math.asin(var))

#function of cos inverse (acos)
def cosInverse(var):
    return (math.acos(var))

#function of tan inverse (atan)
def tanInverse(var):
    return (math.atan(var))

#function for the length of the vector from the origin to point (d)
def magnitude(varOne,varTwo):
    length = math.hypot(varOne,varTwo)
    return length

#functions for converting degree to radian & vice versa (d-r) (r-d)
def degreeToRadian(var):
    return (math.radians(var))

def radianToDegree(var):
    return (math.degrees(var))

#functions for hyperbolic functions (sih, cosh, tanh, asinh, acosh, atanh)

def sinHyperbolic(var):
    return (math.sinh(var))

def cosHyperbolic(var):
    return (math.cosh(var))

def tanHyperbolic(var):
    return (math.tanh(var))

def asinHyperbolic(var):
    return (math.asinh(var))

def acosHyperbolic(var):
    return (math.acosh(var))

def atanHyperbolic(var):
    return (math.atan(var))

def secondVar():
    varSecond = input("Enter the second number.")
    try:
        varSecond = float(varSecond)

    except:
        print("invalid second number.")

    return varSecond


def command(firstVariable):
    operator = input("Enter one of the operator given above: ")

    #if the operation is done on a single number
    if (operator == "!") or (operator == "ln") or (operator == "sin") or (operator == "asin") or (operator == "cos") or (operator == "acos") or (operator == "tan") or (operator == "atan") or (operator == "sinh") or (operator == "asinh") or (operator == "cosh") or (operator == "acosh") or (operator == "tanh") or (operator == "atanh") or (operator == "d-r") or (operator == "r-d"):
        if operator == "!":
            answer = (factorial(firstVariable))
            print(answer)

        elif operator == "ln":
            answer = (logrithmBaseE(firstVariable))
            print(answer)

        elif operator == "sin":
            answer = (sin(firstVariable))
            print(answer)

        elif operator == "cos":
            answer = (cos(firstVariable))
            print(answer)

        elif operator == "tan":
            answer = (tan(firstVariable))
            print(answer)

        elif operator == "asin":
            answer = (sinInversse(firstVariable))
            print(answer)

        elif operator == "acos":
            answer = (cosInverse(firstVariable))
            print(answer)

        elif operator == "atan":
            answer = (tanInverse(firstVariable))
            print(answer)

        elif operator == "sinh":
            answer = (sinHyperbolic(firstVariable))
            print(answer)

        elif operator == "cosh":
            answer = (cosHyperbolic(firstVariable))
            print(answer)

        elif operator == "tanh":
            answer = (tanInverse(firstVariable))
            print(answer)
        elif operator == "asinh":
            answer = (asinHyperbolic(firstVariable))
            print(answer)
        elif operator == "acosh":
            answer = (acosHyperbolic(firstVariable))
            print(answer)
        else:
            answer = (atanHyperbolic(firstVariable))
            print(answer)

#if the operation is done on two numbers
    elif (operator == "+") or (operator == "-") or (operator == "*") or (operator == "/") or (operator == "^") or (operator == "1/n") or (operator == "avg") or (operator == "gcd") or (operator == "d") or (operator == "log"):
        secondVariable = secondVar()

        if operator == "+":
            answer = (add(firstVariable, secondVariable))
            print(answer)
        elif operator == "-":
            answer = (subtract(firstVariable, secondVariable))
            print(answer)
        elif operator == "*":
            answer = (multiplication(firstVariable, secondVariable))
            print(answer)
        elif operator == "/":
            answer = (division(firstVariable, secondVariable))
            print(answer)
        elif operator == "^":
            answer = (power(firstVariable, secondVariable))
            print(answer)
        elif operator == "1/n":
            answer = (root(firstVariable, secondVariable))
            print(answer)
        elif operator == "avg":
            answer = (average(firstVariable, secondVariable))
            print(answer)
        elif operator == "gcd":
            answer = (gcd(firstVariable, secondVariable))
            print(answer)
        elif operator == "d":
            answer = (magnitude(firstVariable, secondVariable))
            print(answer)
        elif operator == "log":
            answer = (logrithm(firstVariable, secondVariable))
            print(answer)

    else:
        print("Invalid operator.")

    return answer

def main():
    print("""In this calculator you will first enter a number, than operator and than if required another number.
    You can use the answer of the one question in the next question for maximum of five times.
    Enter \"!\" for factorial \"ln\" for natural log \"sin\"  \"asin\" \"cos\" \"acos\" \"tan\" \"atan\"
    \"sinh\" \"asinh\" \"cosh\" \"acosh" \"tanh\" \"atanh\"
    \"+\" for addition \"-\" for subtraction \"*\" for muliplication \"/\" for division \"^\" for power
    \"1/n\" for nth-root \"avg\" for average \"gcd\" for gcd" \"d\"for magnitude \"log\" for log to some base.

    """)

    firstVariable = input("Enter a number: ")

    flag = True
    try:
        firstVariable = float(firstVariable)

    except:
        print("Invalid number.")
        flag = False

    if flag == True:
        answer = command(firstVariable)

    #using answer of first calculation in next calculations.

        secondCalculation = input("Do you want to apply another operation on the answer. Write \"T\" for yea and \"F\" for no.")

        if secondCalculation == "T" or secondCalculation == "t":
            command(answer)

            thirdCalculation = input("Do you want to apply another operation on the answer. Write \"T\" for yea and \"F\" for no.")

            if thirdCalculation == "T" or thirdCalculation == "t":
                command(answer)

                fourthCalculation = input("Do you want to apply another operation on the answer. Write \"T\" for yea and \"F\" for no.")

                if fourthCalculation == "T" or fourthCalculation == "t":
                    command(answer)

                    fifthCalculation = input("Do you want to apply another operation on the answer. Write \"T\" for yea and \"F\" for no.")

                    if fifthCalculation == "T" or fifthCalculation == "t":
                        command(answer)

main()
