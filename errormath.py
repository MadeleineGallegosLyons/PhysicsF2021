import math

def rule1():
    constant = float(input('enter constant or quantity with negligible uncertainty: '))
    quantityA = float(input('enter measurement A: '))
    uncertainty_in_A = float(input('enter uncertainty of measurement A: '))
    print('the uncertainty of this equation is ', constant*uncertainty_in_A)

def rule2():
    constant = float(input('enter the constant: '))
    exponent = float(input('enter the exponent: '))
    quantityA = float(input('enter measurement A: '))
    uncertainty_in_A = float(input('enter uncertainty of measurement A: '))
    print('the uncertainty of this equation is ', exponent*(uncertainty_in_A/quantityA))

def rule4():
    constant = float(input('enter the constant: '))
    quantityA = float(input('enter measurement A: '))
    uncertainty_in_A = float(input('enter uncertainty of measurement A: '))
    exponentA = float(input('enter exponent for first expression: '))
    quantityB = float(input('enter measurement B: '))
    uncertainty_in_B = float(input('enter uncertainty of measurement B: '))
    exponentB = float(input('enter exponent for second expression: '))
    error = math.sqrt(((exponentA*(uncertainty_in_A/quantityA))**2) + (exponentB*(uncertainty_in_B/quantityB)**2))
    print('the uncertainty of this equation is ', error)
    
def choose_rule(selection):
    if selection == '1':
        rule1()
    elif selection == '2':
        rule2()
    elif selection == '4':
        rule4()

def main():
    print("Rule 1: If Q = cA where c is a constant (or a quantity with negligible uncertainty), /n then δQ/|Q| = δA/|A| or equivalently δQ = |c|δA")
    print("Rule 2: If Q = cA^m where c and m are constants, then δQ/|Q| = |m|*(δA/|A|) or equivalently δQ = |cmA^(m−1)|δA")
    print("Rule 4: If Q = cAmBn where c, m, and n are constants, then it's the long one.")
    choose_rule(input("Please type '1', '2', or '4': "))

if __name__ == "__main__":
    main()

    
