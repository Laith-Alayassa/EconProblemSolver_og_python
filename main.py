from sympy import *
from sympy.abc import ns


# TODO: make it so that you can input the equations in different forms, either revenue equation directly or price equation
# TODO: calculate welfare loss
def solveProfitMax(problem ="profitMax"):  # TODO: Make them one function depending on the condition
    if problem == "monopoly":
        print('\n You are solving a profit maximization problem for a monopoly')
    else:
        print("\n You are solving a profit maximization problem")
    # Create unknown variable as a symbol
    Q = symbols("Q")  # symbol means the same thing as a variable in normal language

    # Set up equations

    print("example input for price function: 100 * Q - 4")
    print("example input for cost function: Q ^ 2 + 4 * Q - 3 \n")

    ns["Q"] = Symbol("Q")
    price = sympify(  # price function
        input("What is the price equation? (FORM: m*Q -b), where Q is quantity: ")
            .replace("^", "**")
            .replace("q", "Q"),
        locals=ns)  # TODO: setup formula using the default demand equation formula Q = mP + b <-> p = (Q-b)/m
    cost = sympify(
        input("What is the cost equation? ")
            .replace("^", "**")
            .replace("q", "Q"), locals=ns)

    p = 0  # price
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
    q = 0
    for x in quantities:
        if x >= 0:
            print(f"Q could be: {x} units")
            print(f"Q could be: {N(x, 3)} units")
        if x > 0:
            q = x

    p = price.subs(Q, q)  # finding price

    # replacing Q in cost with found quantity value
    costText = str(cost).replace("Q", "(" + str(q) + ")")  # TODO: just use cost and revenue instead of new variables
    revenueText = str(revenue).replace("Q", "(" + str(q) + ")")

    # find profit with found quantity
    profit = eval(revenueText) - eval(costText)

    # Print output
    print("\n")
    print("Profit = P * Q - C")
    print(f"Profit = {revenueText.replace('**', '^')} - ({costText.replace('**', '^')})")
    print(f"profit = ${profit}")
    print(f"profit = ${N(profit, 5)}")

    if problem == "monopoly":
        def findWelfareLoss():
            a = p  # upper corner substitute Q into the MC (derivative of cost function)
            print(f"a = {a}")
            c = diff(cost).subs(Q, q)  # lower  corner where MC is evaluated at new Q
            print(f"c = {c}")
            b = solve(diff(cost) - price, Q)  # right corner of the triangle
            print(f"b = {b}, and it's type is {type(b)}")
            print(f"b[0] = {b[0]}")
            print(f"q = {q}, and its type is {type(q)}")

            b = b[0]
            welfareLoss = 1 / 2 * (a - c) * (b - q)  # b-q because q is the monopoly quant and b is the free market quant

            print(f"\nWelfare loss is equal to {welfareLoss}")

        findWelfareLoss()

if __name__ == '__main__':
    solveProfitMax("monopoly")
