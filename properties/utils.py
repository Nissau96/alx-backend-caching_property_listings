# properties/utils.py

from django.core.cache import cache
from .models import Property
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def get_all_properties():
    """
    Retrieves all properties from the cache if available,
    otherwise queries the database and caches the result for 1 hour.
    """
    cache_key = 'all_properties'
    properties = cache.get(cache_key)

    if properties is None:
        # Data is not in the cache, so fetch from the database
        logger.info("Cache miss for 'all_properties'. Querying database.")
        properties = Property.objects.all().order_by('-created_at')

        # Store the queryset in the cache for 1 hour (3600 seconds)
        cache.set(cache_key, properties, 3600)
    else:
        # Data was found in the cache
        logger.info("Cache hit for 'all_properties'. Serving from cache.")

    return properties