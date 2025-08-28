# properties/views.py

from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties


# Cache this view for 15 minutes
@cache_page(60 * 15)
def property_list(request):
    """
    Returns a JSON response containing a list of all properties.

    This view leverages low-level caching for the queryset and view-level
    caching for the final JSON response.
    """
    # Use the utility function to get properties (from cache or DB)
    properties = get_all_properties()

    properties_data = [
        {
            'title': prop.title,
            'description': prop.description,
            'price': str(prop.price),
            'created_at': prop.created_at.isoformat(),
        }
        for prop in properties
    ]

    return JsonResponse({'properties': properties_data})