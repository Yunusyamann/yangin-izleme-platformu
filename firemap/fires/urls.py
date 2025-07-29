from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('api/firepoints/', views.firepoints_api, name='firepoints_api'),
]
