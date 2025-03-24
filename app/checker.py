from flask import session
from functools import wraps


def check_logged_in(func):
    # New decorator function receives a function as argument
    # Wraps decorator needed! always!
    @wraps(func)
    # We define a 'wrapper' function that receives the arguments of the wrapped function
    def wrapper(*args, **kwargs):
        # Inside 'wrapper' we do the new logic and
        # we finish calling the wrapped function to do it function
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    # At the end of the decorator we return the 'wrapper' function
    return wrapper
