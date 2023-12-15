def logger(iters):

    def actual_decorator(function):

        print(iters)
        def wrapper(*args, **kwargs):
            print('hello from decorator before function call')
            result = function(*args, **kwargs)
            print(f'result:{result}')
            print('bay from decorator after function call')
            return result
        return wrapper

    return actual_decorator

@logger(iters=1)
def sum(a, b):
    return a+b

if __name__ == "__main__":
    sum(4, 5)
