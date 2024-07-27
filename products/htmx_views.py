from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def check_product(request):
    product = request.GET.get('product')
    products = Product.objects.filter(name=product)
    return render(request, 'partials/htmx_components/check_product.html', {'products': products})

def save_product(request):
    name = request.POST.get('product')
    price = request.POST.get('price')

    product = Product(
        name=name,
        price=price
    )

    product.save()
    products = Product.objects.all()
    return render(request, 'partials/htmx_components/list_all_products.html', {'products': products})

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    products = Product.objects.all()
    return render(request, 'partials/htmx_components/list_all_products.html', {'products': products})