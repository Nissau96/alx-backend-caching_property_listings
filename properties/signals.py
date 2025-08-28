# properties/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property
import logging

logger = logging.getLogger(__name__)

def invalidate_property_cache(sender, instance, **kwargs):
    """
    Invalidates the 'all_properties' cache.
    This function is connected to post_save and post_delete signals for the Property model.
    """
    cache_key = 'all_properties'
    if cache.get(cache_key):
        cache.delete(cache_key)
        logger.info(f"Cache invalidated for '{cache_key}' due to change in property {instance.id}.")

# Connect the invalidate_property_cache function to the post_save signal
post_save.connect(invalidate_property_cache, sender=Property)

# Connect the invalidate_property_cache function to the post_delete signal
post_delete.connect(invalidate_property_cache, sender=Property)