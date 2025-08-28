from django.apps import AppConfig


class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'

    def ready(self):
        """
        This method is called when Django starts.
        We import our signals module here to ensure the signal handlers are connected.
        """
        import properties.signals