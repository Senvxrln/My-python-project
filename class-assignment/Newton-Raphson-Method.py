# Find the root of the function x**3 + 3x + 2 using newton-raphson method
import time
import psutil
def f(x):
    return x**3 - 6*x**2 + 8*x + 0.8

def df(x):
    return 3*x**2 - 12*x + 8

#performance monitoring
cpu_usage_i = psutil.cpu_percent(interval=0.1)
ram_usage_i = psutil.virtual_memory().percent

print("CPU Usage_i:", cpu_usage_i, "%")
print("RAM Usage_i:", ram_usage_i, "%")

# parameters
tol = 10**-10 #tolerance
max_iter = 100 # maximum iteration 
itr = 0 # iteration counter
x = float(input("Initial guess: ")) # initial guess
result = f(x)

# finding root
i_time = time.perf_counter()
while abs(result) > tol and itr < max_iter:
   itr += 1
   result = f(x)
   print("Iteration:", itr, "x:", x, "f(x):", result)
   x_new = x - result/df(x) # newton-raphson formula
   x = x_new
   if df(x) == 0:
        print("Turunan bernilai nol.")
        break

if abs(result) < tol:
       print("Root found:", x, "after:", itr, " iterations")

else:
     print("Root not found after:", itr, " iterations")

f_time = time.perf_counter()
print("Execution time:", f_time - i_time, "seconds")

cpu_usage_f = psutil.cpu_percent(interval=0.1)
ram_usage_f = psutil.virtual_memory().percent

print("CPU Usage_f:", cpu_usage_f, "%")
print("RAM Usage_f:", ram_usage_f, "%")
