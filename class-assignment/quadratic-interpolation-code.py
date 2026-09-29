import numpy as np

def f(x):
    return np.exp(x) - 3*x

# initial bracket and point selection
x = np.array([-2.0, 1.0, 2.0])

# setting parameter
tol = 10**-6
itr = 0
max_itr = 100

while itr < max_itr:
    # setting lagrange interpolation
    numerator = (
            (x[1]**2 - x[2]**2) * f(x[0]) + 
            (x[2]**2 - x[0]**2) * f(x[1]) + 
            (x[0]**2 - x[1]**2) * f(x[2])
        )
    denominator = (
            (x[1] - x[2]) * f(x[0]) + 
            (x[2] - x[0]) * f(x[1]) + 
            (x[0] - x[1]) * f(x[2])
        )
    x_ = 0.5*(numerator/denominator)

    if denominator == 0:
        print("Denominator is zero")

    # setting tolerance
    er = abs(x_ - x[1])

    # checking for convergence
    if er < tol:
        print(f"Root found after {itr} iterations: {x_} with function value: {f(x_)}")
        break

    # updating the bracket
    if x_ > x[1]:
        if f(x_) < f(x[1]):
                x[0] = x[1]
                x[1] = x_
        else:
                x[2] = x_
    elif x_ < x[1]:
        if f(x_) < f(x[1]):
                x[2] = x[1]
                x[1] = x_
        else:
                x[0] = x_
    # counting iteration for each update
    itr += 1
    print(f"Iteration: {itr},   x: {x_},    f(x): {f(x_)},   e: {er}")
else:
    print(f"root not found after {itr}, iteration")
