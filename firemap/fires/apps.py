from django.apps import AppConfig

class FiresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fires'

    def ready(self):
        from . import startup
