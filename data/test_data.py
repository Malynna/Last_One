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

    personal_data= {
        "tax_id" : (random_generator.tax_id),
        "company" : (random_generator.company),
        "first_name": (random_generator.first_name),
        "last_name": (random_generator.last_name),
        "address_1": (random_generator.address_1),
        "address_2": (random_generator.address_2),
        "postal_code": (random_generator.postal_code),
        "city": (random_generator.city),
        "email": (random_generator.email),
        "phone": (random_generator.phone)
    }