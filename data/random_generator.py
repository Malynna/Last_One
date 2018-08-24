import string
from random import *


class Random_generator:
    def random_chars(min_chars, max_chars):
        allchars = string.ascii_letters + string.digits
        return "".join(choice(allchars) for x in range(randint(min_chars, max_chars)))

    def random_digits( min_chars, max_chars):
        return "".join(choice(string.digits) for x in range(randint(min_chars, max_chars)))

    new_product = "P " + random_chars(4, 8)
    price = random_digits(1 ,3)
    tax_id = random_digits(3 ,7)
    company = "Com " + random_chars(4, 8)
    first_name = random_chars(8, 10)
    last_name = random_chars(4, 8)
    address_1 = random_chars(4, 8)
    address_2 = random_chars(4, 8) + random_digits(1,3)
    postal_code = random_digits(2,2) + "-" + random_digits(3,3)
    city = random_chars(8, 10)
    email = random_chars(5, 10) + "@" + random_chars(2, 5) + "." + random_chars(2, 3)
    phone = "+" + random_digits(11,11)