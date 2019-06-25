from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "los_precios.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import los_precios.users.signals  # noqa F401
        except ImportError:
            pass
