from django.shortcuts import render
from .models import Product

def home(request):
    """Pobiera wszystkie produkty z bazy i wysyła je do szablonu."""
    products = Product.objects.all()
    return render(request, 'sklep/home.html', {'products': products})