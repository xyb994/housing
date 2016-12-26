from django.apps import AppConfig


class ListingsConfig(AppConfig):
    name = 'ssu_housing.listings'
    verbose_name = "Listing"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
