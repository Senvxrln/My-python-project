import numpy as np
import time
import psutil

def f(t):
    return 60*np.tan(t) - 23.184*(1/np.cos(t))**2 - 0.5

#performance monitoring (initial)
cpu_usage_i = psutil.cpu_percent(interval=0.1)
ram_usage_i = psutil.virtual_memory().percent


# parameters
tol = 10**-12  # tolerance
max_iter = 100  # maximum iteration
itr = 0 
t = float(input("Initial guess(radian): "))  # initial guess
result = f(t)



# finding theta

# initial time
i_time = time.perf_counter()

while abs(result) > tol and itr < max_iter:
    itr += 1
    result = f(t)
    t = t - (result**2)/(f(t + result) - result)
    t = t % (np.pi / 2) # restrict the value to be between 0 and pi/2
    print(f"iteration: {itr},   result: {result}")
    
    if f(t + result) - result == 0:
        print("Penyebut bernilai 0")
        break

    if abs(result) < tol:
        print(f"Root found: {t} rad, after: {itr} iterations")

# final time
f_time = time.perf_counter()

# performance monitoring (final)
cpu_usage_f = psutil.cpu_percent(interval=0.1)
ram_usage_f = psutil.virtual_memory().percent


# time and performance
per_time = f_time - i_time
print(f"\nExecution time:", {per_time}, "seconds")

print("CPU Usage_i:", cpu_usage_i, "%")
print("RAM Usage_i:", ram_usage_i, "%")
print("CPU Usage_f:", cpu_usage_f, "%")
print("RAM Usage_f:", ram_usage_f, "%")




