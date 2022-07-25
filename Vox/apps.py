from django.apps import AppConfig


class VoxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Vox'

    def ready(self):
        import Vox.signals
