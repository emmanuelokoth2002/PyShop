from django.test import TestCase
from products.models import Product, Offer

class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(name="Apple", price=30, stock=20, image_url="http://example.com/image.jpg")
    
    def test_product_creation(self):
        product = Product.objects.get(name="Apple")
        self.assertEqual(product.price, 30)
        self.assertEqual(product.stock, 20)
        self.assertEqual(product.image_url, "http://example.com/image.jpg")
        
class OfferModelTest(TestCase):
    def setUp(self):
        Offer.objects.create(code="Discount10",description='10% discount on all items',discount=10.0)
        
    def test_offer_creation(self):
        offer = Offer.objects.get(code="Discount10")
        self.assertEqual(offer.description, "10% discount on all items")
        self.assertEqual(offer.discount, 10.0)       