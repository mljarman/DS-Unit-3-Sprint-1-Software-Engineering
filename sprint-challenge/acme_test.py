import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_weight(self):
        """
        Tests default value of weight within Product class.
        """
        prod2 = Product('Test2')
        self.assertEqual(prod2.weight, 20)

    def test_stealability_and_explode(self):
        """
        Tests product's stealability and how big its explosion will be.
        """
        prod3 = Product('Test3', price=15, flammability=1)
        self.assertEqual(prod3.stealability(), 'Kinda stealable')
        self.assertEqual(prod3.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """
    Tests product and inventory report's functionality.
    """
    def test_default_num_products(self):
        """
        Makes sure list contains 30 values.
        """
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """
        Verifies product names are in correct format with 1 ADJECTIVE, 1 NOUN.
        """
        products = generate_products()
        for product in products:
            adj = product.split(" ")[0]
            noun = product.split(" ")[1]
        self.assertIn(adj, ADJECTIVES)
        self.assertIn(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()


