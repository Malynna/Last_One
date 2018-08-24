import string
from random import *


class RandomGenerator:
    def random_chars(min, max):
        allchars = string.ascii_letters + string.digits
        return "".join(choice(allchars) for x in range(randint(min, max)))

    def random_digits( min, max):
        return "".join(choice(string.digits) for x in range(randint(min, max)))

    new_product = "P " + random_chars(4, 8)
    price = random_digits(1 ,3)
    tax_id = "PL" + random_digits(10 ,10)
    company = "Com " + random_chars(4, 8)
    first_name = random_chars(8, 10)
    last_name = random_chars(4, 8)
    address_1 = random_chars(4, 8)
    address_2 = random_chars(4, 8) + random_digits(1,3)
    postal_code = random_digits(2,2) + "-" + random_digits(3,3)
    city = random_chars(8, 10)
    email = random_chars(5, 10) + "@" + random_chars(2, 5) + "." + random_chars(2, 3)
    phone = "+" + random_digits(11,11)