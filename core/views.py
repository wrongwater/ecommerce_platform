from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from .models import Category

# Create your views here.
def index(request):
    categories = Category.objects.all()[:12]
    return render(request, 'core/index.html', {'categories': categories})


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


def page(request, page_name):
    """Render mock pages."""
    page_content = {
        'about': {
            'title': 'About Us',
            'heading': 'About Organic Grocery Store',
            'content': 'We are committed to providing fresh, organic products to your doorstep. Our mission is to promote healthy living through quality organic produce and products.'
        },
        'contact': {
            'title': 'Contact Us',
            'heading': 'Get in Touch',
            'content': 'Email: info@organicstore.com\nPhone: (555) 123-4567\nAddress: 123 Green Street, Garden City, ST 12345'
        },
        'faq': {
            'title': 'Frequently Asked Questions',
            'heading': 'FAQ',
            'content': 'Q: Do you offer delivery?\nA: Yes, we deliver to all areas within 10 miles.\n\nQ: Are all products organic?\nA: Yes, all our products are certified organic.\n\nQ: What is your return policy?\nA: We offer 30-day returns on all products.'
        },
        'shipping': {
            'title': 'Shipping Information',
            'heading': 'Shipping & Delivery',
            'content': 'Free shipping on orders over $50. Standard delivery takes 2-3 business days. Express delivery available for urgent orders. All packages are insured and tracked.'
        },
        'returns': {
            'title': 'Returns Policy',
            'heading': 'Returns & Refunds',
            'content': 'We offer a 30-day money-back guarantee on all products. Items must be in original condition. Refunds are processed within 5-7 business days.'
        },
        'privacy': {
            'title': 'Privacy Policy',
            'heading': 'Your Privacy Matters',
            'content': 'We protect your personal information and never share it with third parties. Your data is encrypted and stored securely. Read our full privacy policy for details.'
        }
    }
    
    data = page_content.get(page_name, {'title': 'Page Not Found', 'heading': 'Page Not Found', 'content': 'The page you are looking for does not exist.'})
    return render(request, 'core/page.html', data)


def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def shop(request):
    return render(request, "core/shop.html")

def cart(request):
    return render(request, "core/cart.html")

def checkout(request):
    return render(request, "core/checkout.html")

def login_view(request):
    return render(request, "core/login.html")

def register(request):
    return render(request, "core/register.html")