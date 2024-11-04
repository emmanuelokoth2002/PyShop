from django.urls import reverse
from django.test import TestCase
from products.views import index, new
from products.models import Product

class ProductListViewTest(TestCase):
    def setUp(self):
        Product.objects.create(name="Banana", price=20, stock=50, image_url="http://example.com/image.jpg")
        Product.objects.create(name="Orange", price=50, stock=30, image_url="http://example.com/image.jpg")
        
    def test_index_view(self):
        """Test that the index view returns a 200 status and uses the correct template."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('products', response.context)
        self.assertEqual(len(response.context['products']), 2)
          
    def test_new_view(self):
        """Test that the new view returns a 200 status and the expected HttpResponse content."""
        response = self.client.get(reverse('new'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"New products")