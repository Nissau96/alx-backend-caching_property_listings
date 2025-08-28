from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
import uuid


class Property(models.Model):
    """
    Property model representing real estate listings.

    This model includes fields commonly found in property listing platforms
    and is optimized for caching scenarios.
    """

    # Use UUID for better security and caching keys
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(
        max_length=200,
        help_text="Property title (max 200 characters)",
        db_index=True  # Index for faster queries
    )

    description = models.TextField(
        help_text="Detailed property description"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Property price in USD",
        db_index=True  # Index for price-based queries
    )

    location = models.CharField(
        max_length=100,
        help_text="Property location",
        db_index=True  # Index for location-based queries
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when property was created"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when property was last modified"
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Whether the property listing is active",
        db_index=True
    )

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['location', 'price']),
            models.Index(fields=['is_active', 'created_at']),
        ]

    def __str__(self):
        return f"{self.title} - {self.location} (${self.price})"

    def get_absolute_url(self):
        return reverse('property-detail', kwargs={'pk': self.pk})

    @property
    def cache_key(self):
        """Generate cache key for this property instance."""
        return f"property:{self.pk}"

    @classmethod
    def get_list_cache_key(cls, **filters):
        """Generate cache key for property list queries."""
        filter_str = "_".join(f"{k}:{v}" for k, v in sorted(filters.items()))
        return f"properties:list:{filter_str}" if filter_str else "properties:list:all"