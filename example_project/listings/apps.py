from django.apps import AppConfig


class ListingsConfig(AppConfig):
    name = 'example_project.listings'
    verbose_name = "Listing"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
