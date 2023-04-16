"""
Test the main module.
OG Author: Wolf Paulus (https://wolfpaulus.com)
New Hip Author: Marcello Novak (idonthaveawebsite.idk)
"""
from unittest import TestCase
from __main__ import is_prime, is_prime_str


class Test(TestCase):
    def test_is_prime(self):
        assert not is_prime(0)
        assert is_prime(7)
        assert not is_prime(16)

    def test_is_prime_str(self):
        assert is_prime_str("11") == "11 is prime."
        assert is_prime_str("13") == "13 is prime."
        assert is_prime_str("20") == "20 is not prime."
        assert is_prime_str("-1") == "Please enter a number."
        assert is_prime_str("A") == "Please enter a number."
        assert is_prime_str("") == "Please enter a number."
