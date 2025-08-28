# properties/views.py

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Property

# Cache this view for 15 minutes
@cache_page(60 * 15)
def property_list(request):
    """
    Displays a list of all properties.

    The response of this view is cached for 15 minutes. Subsequent requests
    within this timeframe will be served directly from the Redis cache,
    avoiding database queries and template rendering.
    """
    properties = Property.objects.all().order_by('-created_at')
    context = {
        'properties': properties
    }
    return render(request, 'properties/property_list.html', context)