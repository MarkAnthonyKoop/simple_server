import os

def trace_function(func):
    def wrapper(*args, **kwargs):
        with open('trace_function.log', 'a') as log_file:
            log_file.write(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}\n")
        result = func(*args, **kwargs)
        with open('trace_function.log', 'a') as log_file:
            log_file.write(f"{func.__name__} returned: {result}\n")
        return result
    return wrapper
