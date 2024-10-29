from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ScaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.sca'
    verbose_name = _("Sca")
