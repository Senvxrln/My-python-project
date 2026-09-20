import numpy as np
import time

def f(t):
    return 60*np.tan(t) - 23.184*(1/np.cos(t))**2 - 0.5

# parameters
tol = 10**-12  # tolerance
max_iter = 100  # maximum iteration
itr = 0 
t = float(input("Initial guess(radian): "))  # initial guess
result = f(t)

# finding theta
i_time = time.perf_counter()

while abs(result) > tol and itr < max_iter:
    itr += 1
    result = f(t)
    t = t - (result**2)/(f(t + result) - result)
    t = t % (np.pi / 2) # restrit the value to be between 0 and pi/2
    print(f"iteration: {itr},   result: {result}")
    
    if f(t + result) - result == 0:
        print("Penyebut bernilai 0")
        break

    if abs(result) < tol:
        print("Root found:", t, "after:", itr, " iterations")


f_time = time.perf_counter()
per_time = f_time - i_time

print(f"\nExecution time:", {per_time}, "seconds")
