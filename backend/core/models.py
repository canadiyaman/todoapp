from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils import TimeStampModel


class Todo(TimeStampModel):
    title = models.CharField(verbose_name=_('title'), max_length=500)
    body = models.TextField(verbose_name=_('body'), null=True, blank=True)
    is_completed = models.BooleanField(verbose_name=_('is completed'), default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']
        verbose_name = _('todo')
        verbose_name_plural = _('todos')
