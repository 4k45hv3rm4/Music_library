from django.urls import path
from cd_library import views
urlpatterns = [
    path('cd/', views.index, name='index'),
    path('cd/<int:id>/', views.detail, name='detail'),
    ]
