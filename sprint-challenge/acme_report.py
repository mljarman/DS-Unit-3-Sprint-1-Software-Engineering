from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products()

    return products


def inventory_report(names, prices, weights, flammabilities):
    """
    takes a list of products and prints a nice summary
    """
    num_products = len(products)
    avg_price = mean(prices)
    avg_weight = mean(weights)
    avg_flammability = mean(flammabilities)


    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: {}".format(num_products))
    print("Average price: {}".format(avg_price))
    print("Average weight: {}".format(avg_weight))
    print("Average flammability: {}".format(avg_flammability))


if __name__ == '__main__':
    inventory_report(generate_products())