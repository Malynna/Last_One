import string
from random import *


class random_generator:
    def random_chars(min_chars, max_chars):
        allchars = string.ascii_letters + string.digits
        return "".join(choice(allchars) for x in range(randint(min_chars, max_chars)))

    def random_digits( min_chars, max_chars):
        return "".join(choice(string.digits) for x in range(randint(min_chars, max_chars)))