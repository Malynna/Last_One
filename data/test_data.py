from data.random_generator import random_generator




class test_data(random_generator):


    categories = {
        "phones": "category-1",
        "lukasz": "category-3"
    }

    products = {
        "first" : "Mi A1",
        "second" : "Mi 8",
        "third" : "Mi Mix 2S",
        "new_product" : (random_generator.new_product),
        "price" : (random_generator.price)
    }