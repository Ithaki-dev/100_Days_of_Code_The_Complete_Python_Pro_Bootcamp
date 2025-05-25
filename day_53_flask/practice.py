import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.2f} seconds")
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

if __name__ == "__main__":
    fast_function()
    slow_function()
    print("Execution completed.")