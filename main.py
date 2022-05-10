from sympy import *
from sympy.abc import ns


def profitMaximize():
    print('\n')

    # Create unknown variable as a symbol
    Q = symbols("Q") # symbol means the same thing as a variable in normal language

    # Set up equations
    # TODO: setup formula using the default demand equation formula Q = mP + b <-> p = (Q-b)/m

    ns["Q"] = Symbol("Q")
    price = sympify(input("What is the price equation? (FORM: m*Q -b): "), locals = ns)
    cost = sympify(input("What is the cost equation? ") , locals = ns)

    # price = 100 * Q
    # cost = Q ** 2 + 2 * Q + 50

    revenue = price * Q
    profit = revenue - cost

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

    Q = 0
    for x in quantities:
        if x >= 0:
            print(f"Q could be: {x} units")
        if x > 0:
            Q = x  # Set Q for the positive Q quantity (to eliminate 0 as a possible solution if there is a positive one)
    # replacing Q in cost with found quantity value
    costText = str(cost).replace("Q", str(Q))
    revenueText = str(revenue).replace("Q", str(Q))
    # TODO: Use subs() instead
    # TODO: maybe just use cost and revenue instead of new variables


    # find profit with found quantity
    profit = eval(revenueText) - eval(costText)

    # Print output
    print("\n")
    print("Profit = P * Q - C")
    print(f"Profit = {revenueText} - ({costText})")
    print(f"profit = ${profit}")
    print(f"profit = ${N(profit,5)}")

if __name__ == '__main__':
    profitMaximize()
    # TODO: make it so that this takes in the input

