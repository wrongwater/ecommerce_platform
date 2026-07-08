from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from .models import Category

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def category(request):
    """Render category page if template exists; otherwise fall back to index."""
    try:
        return render(request, 'core/category.html')
    except TemplateDoesNotExist:
        return render(request, 'core/index.html')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'core/category_list.html', {'categories': categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(available=True)
    return render(request, 'core/category_detail.html', {'category': category, 'products': products})