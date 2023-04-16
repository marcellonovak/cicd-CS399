"""
Prime checker
OG Author: Wolf Paulus (https://wolfpaulus.com)
New Hip Author: Marcello Novak (idonthaveawebsite.idk)
"""


def is_prime(n) -> bool:
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_str(num: str) -> str:
    """Return a string indicating whether num is odd or even."""
    if num.isnumeric():
        return f"{num} is {'prime' if is_prime(int(num)) else 'not prime'}."
    else:
        return "Please enter a number."
