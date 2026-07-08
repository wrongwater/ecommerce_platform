from django.shortcuts import render
from django.template import TemplateDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def category(request):
    """Render category page if template exists; otherwise fall back to index."""
    try:
        return render(request, 'core/category.html')
    except TemplateDoesNotExist:
        return render(request, 'core/index.html')
