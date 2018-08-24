from data.random_generator import Random_generator




class Test_data(Random_generator):


    categories = {
        "phones": "category-1",
        "lukasz": "category-3"
    }

    products = {
        "first": "Mi A1",
        "second": "Mi 8",
        "third": "Mi Mix 2S",
        "new_product": (Random_generator.new_product),
        "price": (Random_generator.price)
    }

    personal_data= {
        "tax_id": (Random_generator.tax_id),
        "company": (Random_generator.company),
        "first_name": (Random_generator.first_name),
        "last_name": (Random_generator.last_name),
        "address_1": (Random_generator.address_1),
        "address_2": (Random_generator.address_2),
        "postal_code": (Random_generator.postal_code),
        "city": (Random_generator.city),
        "email": (Random_generator.email),
        "phone": (Random_generator.phone)
    }