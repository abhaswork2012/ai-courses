from app.models import Product
from django.db.models import Q
def search(name=None, min_price=None, max_price=None):
    # Write your code here
    query = Q(is_active=True)
    if name:
        query &= Q(name__icontains=name)
    if min_price is not None:
        query &= Q(price__gte=min_price)
    if max_price is not None:
        query &= Q(price__lte=max_price)
    return Product.objects.filter(query).order_by('price','name')
def newest(n):
    # Write your code here
    return Product.objects.filter(is_active=True).order_by('-created_at','name')[:n]
def price_list(category):
    # Write your code here
    return Product.objects.filter(category=category,is_active=True).order_by('-price','name').values('sku','name','price')
def names_in_category(category):
    # Write your code here
    return Product.objects.filter(category=category,is_active=True).values_list('name',flat=True).order_by('name')
def get_by_sku(sku):
    # Write your code here
    try:
        return Product.objects.get(sku=sku,is_active=True)
    except:
        return None
def get_by_name(name):
    # Write your code here
    try:
        return Product.objects.get(name=name,is_active=True)
    except Product.DoesNotExist:
        return None
    except Product.MultipleObjectsReturned:
        raise
def cheapest_in_category(category):
    # Write your code here
    try:
        return Product.objects.order_by('price','name').filter(category=category,is_active=True).first()
    except Product.DoesNotExist:
        return None
def category_has_products(category):
    # Write your code here
    return Product.objects.filter(category=category,is_active=True).exists()
def count_in_category(category):
    # Write your code here
    return Product.objects.filter(category=category,is_active=True).count()