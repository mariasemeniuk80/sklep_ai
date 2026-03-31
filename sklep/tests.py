from django.test import TestCase
from django.urls import reverse
from .models import Category, Product

class ShopTests(TestCase):
    """Klasa zawierająca testy dla sklepu."""

    def setUp(self):
        """Przygotowuje dane testowe przed każdym testem."""
        self.category = Category.objects.create(name="Paprocie")
        self.product = Product.objects.create(
            category=self.category, name="Nefrolepis", description="Fajna paproć", price=30.00
        )

    def test_category_name(self):
        """Sprawdza poprawność nazwy kategorii."""
        self.assertEqual(str(self.category), "Paprocie")

    def test_product_data(self):
        """Sprawdza poprawność danych produktu."""
        self.assertEqual(self.product.name, "Nefrolepis")
        self.assertEqual(self.product.price, 30.00)

    def test_product_category_relation(self):
        """Sprawdza powiązanie produktu z kategorią."""
        self.assertEqual(self.product.category.name, "Paprocie")

    def test_home_page_status(self):
        """Sprawdza czy strona główna działa (kod 200)."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        """Sprawdza czy użyto dobrego szablonu."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'sklep/home.html')