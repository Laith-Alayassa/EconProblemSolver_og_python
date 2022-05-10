from sympy import *
from sympy.abc import ns


def profitMaximize():
    print('\n')

    # Create unknown variable as a symbol
    Q = symbols("Q") # symbol means the same thing as a variable in normal language

    # Set up equations


    print("example input for price function: 100 * Q - 4")
    print("example input for cost function: Q ** 2 + 4 * Q - 3 \n")

    ns["Q"] = Symbol("Q")
    price = sympify(input("What is the price equation? (FORM: m*Q -b), where Q is quantity: "), locals = ns)     # TODO: setup formula using the default demand equation formula Q = mP + b <-> p = (Q-b)/m
    cost = sympify(input("What is the cost equation? ") , locals = ns)

    revenue = price * Q

    # write solving process
    print("Profit = Revenue - Cost")
    print("Profit = P * Q - Cost\n")
    print("max Profit =\n∆ Profit/ ∆ Q = 0\nMR - MC = 0\n")
    print("max Profit = MR - MC = 0")
    print(f"max Profit = {diff(revenue)} - ({diff(cost)}) = 0")
    print(f"max Profit = {diff(revenue)} = {diff(cost)}")

    # Solve for possible quantities
    quantities = solve(diff(revenue) - diff(cost), Q)

    print("\n")

    # find possible quantities solutions (could be 0 or higher, if higher choose the higher)
    Q = 0
    for x in quantities:
        if x >= 0:
            print(f"Q could be: {x} units")
        if x > 0:
            Q = x

    # replacing Q in cost with found quantity value
    costText = str(cost).replace("Q", "(" + str(Q) + ")")    # TODO: just use cost and revenue instead of new variables
    revenueText = str(revenue).replace("Q", "(" + str(Q) + ")")

    # find profit with found quantity
    profit = eval(revenueText) - eval(costText)

    # Print output
    print("\n")
    print("Profit = P * Q - C")
    print(f"Profit = {revenueText.replace('**', '^')} - ({costText.replace('**', '^')})")
    print(f"profit = ${profit}")
    print(f"profit = ${N(profit)}")

if __name__ == '__main__':
    profitMaximize()

