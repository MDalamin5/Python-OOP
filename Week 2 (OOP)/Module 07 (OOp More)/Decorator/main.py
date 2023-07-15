import math
import time


def timer(func):
    def inner(*args, **kwargs):
        print('Time started')
        start = time.time()
        # print(func)
        func(*args, **kwargs)
        print('Timer End')
        end = time.time()
        print(f'Total time taken: {end-start}')
    return inner

# timer()()

@timer
def get_Factorial(n):
    print('Factorial starting')
    result = math.factorial(n)
    print(f'The factorial of {n}: {result}')
get_Factorial(1220)
# timer(get_Factorial)() 
