from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampModel(models.Model):
    is_active = models.BooleanField(verbose_name=_('is active'), default=True)
    created_at = models.DateTimeField(verbose_name=_('crated at'),
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('updated at'),
                                      auto_now=True)

    class Meta:
        abstract = True
