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


def get_redis_cache_metrics():
    """
    Retrieves and analyzes cache hit/miss metrics from Redis.

    Returns:
        A dictionary containing hits, misses, and the hit ratio.
    """
    try:
        # Get a direct connection to the Redis client
        redis_conn = get_redis_connection("default")

        # Get server statistics
        info = redis_conn.info()

        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)
        total_lookups = hits + misses

        hit_ratio = 0
        if total_lookups > 0:
            hit_ratio = (hits / total_lookups) * 100

        metrics = {
            'hits': hits,
            'misses': misses,
            'total_lookups': total_lookups,
            'hit_ratio': f"{hit_ratio:.2f}%"
        }

        logger.info(f"Redis Cache Metrics: {metrics}")

        return metrics

    except Exception as e:
        logger.error(f"Could not retrieve Redis cache metrics: {e}")
        return {
            'hits': 0,
            'misses': 0,
            'total_lookups': 0,
            'hit_ratio': "0.00%"
        }