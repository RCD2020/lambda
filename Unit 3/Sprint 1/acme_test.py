#!/usr/bin/env python3
"""Tests the acme module and the acme_report module.

Robert Davis 2021/09/03"""


from acme import Product
from acme_report import ADJECTIVES, NOUNS
from acme_report import generate_products, inventory_report


def test_default_product_price():
    """Test default product price being 10."""

    prod = Product('Test Product')
    assert prod.price == 10


def test_based():
    """Test default product values of acme.Product"""

    prod = Product('Testy')
    assert prod.price == 10
    assert prod.weight == 20
    assert prod.flammability == 0.5


def test_steal():
    """Test acme.Product.stealability()
    is working correctly."""

    noSteal = Product('Dumbell', 3, 10)
    maybeSteal = Product('Pliers', 9, 10)
    steal = Product('HoloTV', 3000, 50)

    assert noSteal.stealability() == "Not so stealable..."
    assert maybeSteal.stealability() == "Kinda stealable."
    assert steal.stealability() == "Very stealable!"


def test_boome():
    """Test acme.Product.explode() is working properly."""

    fizzle = Product('Fire Extinguisher', 100, 20, 0)
    sboom = Product('Matches', 1, 2, 6)
    bboom = Product('C4', 300, 20, 10)

    assert fizzle.explode() == "...fizzle."
    assert sboom.explode() == "...boom!"
    assert bboom.explode() == "...BABOOM!!"


def test_default_num_products():
    """Tests if acme_report.generate_products()
    generates 30 products by default."""

    prods = generate_products()

    assert len(prods) == 30


def test_legal_names():
    """Tests that products randomly generated by
    acme_report.generate_products() are legal values."""

    prods = generate_products()

    for prod in prods:
        names = prod.name.split(' ')

        assert names[0] in ADJECTIVES
        assert names[1] in NOUNS


test_prods = [
    Product('Testy', 0, 0, 0),
    Product('Testy', 10, 10, 10),
    Product('Test', 20, 20, 20)
]


def test_inventory_report():
    """Tests if acme_report.inventory_report()
    is calculating correct values."""

    report = inventory_report(test_prods)

    assert report['unique'] == 2
    assert report['m_price'] == 10
    assert report['m_weight'] == 10
    assert report['m_flammability'] == 10
