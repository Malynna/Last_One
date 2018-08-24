from data.random_generator import RandomGenerator


class TestData(RandomGenerator):

    categories = {
        "phones": "category-1",
        "lukasz": "category-3"
    }

    products = {
        "first": "Mi A1",
        "second": "Mi 8",
        "third": "Mi Mix 2S",
        "new_product": (RandomGenerator.new_product),
        "price": (RandomGenerator.price)
    }

    personal_data= {
        "tax_id": (RandomGenerator.tax_id),
        "company": (RandomGenerator.company),
        "first_name": (RandomGenerator.first_name),
        "last_name": (RandomGenerator.last_name),
        "address_1": (RandomGenerator.address_1),
        "address_2": (RandomGenerator.address_2),
        "postal_code": (RandomGenerator.postal_code),
        "city": (RandomGenerator.city),
        "email": (RandomGenerator.email),
        "phone": (RandomGenerator.phone)
    }