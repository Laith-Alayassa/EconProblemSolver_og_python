from sympy import *
from matplotlib import pyplot as plt
from sympy.abc import ns

# plt.style.use('fivethirtyeight')
plt.xkcd()

Q = symbols("Q")
ns["Q"] = Symbol("Q")


def create_plot(price_function, cost_function):

    print(price_function, cost_function)
    print(type(cost_function), type(price_function))

    # Solve for price function intersection
    price_x_intersect = solve(price_function)
    price_y_intersect = price_function.subs(Q, 0)
    print(f"--------- price function x and y: {price_x_intersect}, {price_y_intersect}")

    price_x_intersect = float(price_x_intersect[-1])  # sets x intersect to the lat element of the possible
    # intersections (could do the first as well)

    x_values = [0, price_x_intersect]  # min and max value for x axis
    y_values = [price_y_intersect, 0]  # min and max value for y-axis




    # Solve for MC function intersection
    marginal_cost = diff(cost_function)

    mc_starting_y = marginal_cost.subs(Q, 0)
    mc_ending_y = marginal_cost.subs(Q, price_x_intersect)

    mc_x_values = [0, price_x_intersect]  # min x is at 0, max x is at where P(Q) intersects x
    mc_y_values = [mc_starting_y, mc_ending_y]  # min y is at intersection, max y is where P(
    # Q) intersects y-axis so it doesn't go to infinity, or MC evaluated at Q at price-x0intersection incase the
    # slope of MC is flat

    plt.ylim([0,int(price_y_intersect) * 1.1])
    # TODO: add MR curve

    plt.xlabel("Quantity")
    plt.ylabel("Price")
    plt.plot(x_values, y_values, label="P(Q)")
    plt.plot(mc_x_values, mc_y_values, label="MC(Q)")

    plt.legend()
    plt.tight_layout()

    plt.show()




if __name__ == '__main__':
    create_plot(sympify("-2 * Q**2 + 3", locals=ns),
                sympify('2.5 * Q**2 - 3 ', locals=ns))