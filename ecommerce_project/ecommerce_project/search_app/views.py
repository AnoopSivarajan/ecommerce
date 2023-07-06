

from django.shortcuts import render
from shop_app.models import Product
from django.db.models import Q

def SearchResult(request):
    query = request.GET.get('q')
    products = Product.objects.none()  # Create an empty queryset initially

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))

    context = {'query': query, 'products': products}
    return render(request, 'search.html', context)
