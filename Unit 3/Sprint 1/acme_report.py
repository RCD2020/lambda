"""Generates random products to test the acme classes.

Robert Davis 2021/09/03"""

from random import randint
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(numProducts=30):
    """Generates random acme.Product objects,
    use numProducts to specify how many.\n
    Returns a list of acme.Product."""

    products = []

    for x in range(numProducts):
        adjin = randint(0, len(ADJECTIVES)-1)
        nonin = randint(0, len(NOUNS)-1)

        prod = Product(
            f"{ADJECTIVES[adjin]} {NOUNS[nonin]}",
            randint(5, 101),
            randint(5, 101),
            randint(0, 26) / 10
        )

        products.append(prod)

    return products


def inventory_report(prodList: Product):
    """Takes a list of acme.Product.\n
    Prints a summary of the products.\n
    Returns a dictionary containing the information.\n
    ```json
    {
        "unique": amount of unique,
        "m_price": average price,
        "m_weight": average weight,
        "m_flammability": average flammability
    }
    ```"""

    names = []
    tprice = 0
    tweight = 0
    tflammability = 0

    for prod in prodList:
        if prod.name not in names:
            names.append(prod.name)
        tprice += prod.price
        tweight += prod.weight
        tflammability += prod.flammability
    
    numProd = len(prodList)

    mprice = tprice / numProd
    mweight = tweight / numProd
    mflammability = tflammability / numProd

    info = {
        "unique": len(names),
        "m_price": mprice,
        "m_weight": mweight,
        "m_flammability": mflammability
    }

    print('\033[34mUnique Products:\033[36m', len(names))
    print('\033[34mAverage Price:\033[36m', mprice)
    print('\033[34mAverage Weight:\033[36m', mweight)
    print('\033[34mAverage Flammability:\033[36m', mflammability)
    print('\033[00m', end='')
    return info


if __name__ == '__main__':
    inventory_report(generate_products())
