from django.test import TestCase
from products.views import index, new
from django.urls import reverse, resolve

class ProductUrlTest(TestCase):
    def test_product_list_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
    
    def test_newproduct_entry_url(self):
        url = reverse('new')
        self.assertEqual(resolve(url).func, new)