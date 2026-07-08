from .models import Category

def categories(request):
    return {'site_categories': Category.objects.all()}