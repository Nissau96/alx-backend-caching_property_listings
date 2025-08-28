# properties/urls.py

from django.urls import path
from . import views

# Define the app name for namespacing
app_name = 'properties'

urlpatterns = [
    # Map the root path of this app to the property_list view
    path('', views.property_list, name='property_list'),
]