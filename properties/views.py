# properties/views.py

from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property


# Cache this view for 15 minutes
@cache_page(60 * 15)
def property_list(request):
    """
    Returns a JSON response containing a list of all properties.

    The response of this view is cached for 15 minutes. Subsequent requests
    within this timeframe will be served the cached JSON data directly
    from Redis, avoiding database queries.
    """
    properties = Property.objects.all().order_by('-created_at')

    # Serialize the queryset into a list of dictionaries
    # This format is JSON-friendly
    properties_data = [
        {
            'title': prop.title,
            'description': prop.description,
            'price': str(prop.price),  # Decimals must be converted to strings for JSON
            'created_at': prop.created_at.isoformat(),
        }
        for prop in properties
    ]

    # Return the data as a JSON response
    return JsonResponse({'properties': properties_data})