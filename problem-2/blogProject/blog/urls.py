from django.urls import path, include
from rest_framework import routers
from . import views

# Problem-2 ViewSet + Router을 이용해 API 만들기
router = routers.DefaultRouter()
router.register(r'v1/posts', views.PostViewSet)


urlpatterns=[
    # Problem-2
    path('', include(router.urls)),
]