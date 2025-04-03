from django.urls import path
from .views import add_app, get_apps, delete_app

urlpatterns = [
    path('add-app/', add_app, name='add-app'),
    path('get-apps/', get_apps, name='get-apps'),
    path('delete-app/<int:id>/', delete_app, name='delete-app'),
]
