from rest_framework import serializers
from ..models import Todo

__all__ = ['TodoModelSerializer']


class TodoModelSerializer(serializers.ModelSerializer):
    """
        TodoModelSerializer uses for serialize Todo model data.
        Example List Response
        [
            {
                "id": 1,
                "is_active": true,
                "created_at": "2021-05-02T21:27:23.958898Z",
                "updated_at": "2021-05-02T21:27:23.959576Z",
                "title": "buy some milk",
                "body": "",
                "is_completed": false
            },
            {
                "id": 2,
                "is_active": true,
                "created_at": "2021-05-02T21:27:39.118484Z",
                "updated_at": "2021-05-02T21:27:39.118590Z",
                "title": "this is test title",
                "body": "",
                "is_completed": false
            }
        ]
    """
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_active')
