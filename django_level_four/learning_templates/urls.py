from django.urls import path
from . import views

# define the app name for TEMPLATE TAGGING
app_name = 'learning_templates'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other', views.other, name='other')
]
