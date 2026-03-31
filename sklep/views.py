from django.shortcuts import render
from .models import Category 

def home(request):
    """Pobiera wszystkie kategorie z bazy i wysyła je do szablonu."""
    categories = Category.objects.all()
    return render(request, 'sklep/home.html', {'categories': categories})