import os
import inspect

def trace_function(func):
    def wrapper(*args, **kwargs):
        # Get the function signature and bind the arguments
        func_args = inspect.signature(func).bind(*args, **kwargs)
        func_args.apply_defaults()

        # Construct the arguments string
        args_str = ', '.join(f"{name}={value}" for name, value in func_args.arguments.items())

        # Determine if 'with' should be added
        call_info = f"Calling {func.__name__}"
        if args_str:
            call_info += f" with {args_str}"

        # Log the function call
        with open('trace_function.log', 'a') as log_file:
            log_file.write(call_info + "\n")

        # Call the function and get the result
        result = func(*args, **kwargs)

        # Log the function return
        with open('trace_function.log', 'a') as log_file:
            log_file.write(f"{func.__name__} returned: {result}\n")

        return result
    return wrapper

