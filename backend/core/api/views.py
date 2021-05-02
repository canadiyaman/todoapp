from rest_framework import viewsets

from .serializers import TodoModelSerializer
from ..models import Todo

__all__ = ['TodoViewSet']


class TodoViewSet(viewsets.ModelViewSet):
    """
        TodoViewSet provides enpoints for Todo datas.
    """
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
