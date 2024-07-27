from django.http import HttpResponse
from .models import Product

def check_product(request):
    product = request.GET.get('product')
    products = Product.objects.filter(name=product)
    if products.exists():
        return HttpResponse('This product already exists.')
    return HttpResponse('Product available for registration.')