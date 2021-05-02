from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter

from core.api.views import TodoViewSet

router = DefaultRouter()

router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
