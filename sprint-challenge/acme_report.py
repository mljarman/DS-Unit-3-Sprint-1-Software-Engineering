
import random
from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    generate a list of 30 randomly selected product names
    """
    products = []
    for num in range(num_products):
        product_names = (random.sample(ADJECTIVES, 1)[0] + " " + 
                        random.sample(NOUNS, 1)[0])
        products.append(product_names)
    return products


def inventory_report(products):
    """
    takes a list of products and prints a nice summary
    """
    inventory_list = []

    for product_name in products:
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        prod = Product(product_name,
                      price=price,
                      weight=weight,
                      flammability=flammability)
        inventory_list.append(prod)

    prices = []
    weights = []
    flammabilities = []

    for item in inventory_list:
        prices.append(item.price)
        weights.append(item.weight)
        flammabilities.append(item.flammability)

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:", len(set(products)))
    print("Average price:", sum(prices)/len(prices))
    print("Average weight:", sum(weights)/len(weights))
    print("Average flammability:", sum(flammabilities)/len(flammabilities))


if __name__ == '__main__':
    inventory_report(generate_products())
