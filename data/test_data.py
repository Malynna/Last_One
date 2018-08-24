from data.random_generator import random_generator




class test_data(random_generator):

    product_name = "P " + random_generator.random_chars(4, 8)
    price = random_generator.random_digits(1 ,3)

    categories = {
        "XiaomiLepsze": "category-1",
        "Lukasz": "category-3"
    }

    products = {
        "first" : "Mi A1",
        "second" : "Mi 8",
        "third" : "Mi Mix 2S"
    }