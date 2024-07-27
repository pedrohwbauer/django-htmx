from django.urls import path
from . import views
from . import htmx_views

urlpatterns = [
    path('list_products', views.list_products, name ='list_products')
]

htmx_urlpatterns = [
    path('check_product', htmx_views.check_product, name='check_product')
    # path('save_product/', )
]

urlpatterns = urlpatterns + htmx_urlpatterns