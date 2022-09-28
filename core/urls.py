from django.urls import path, include

from . import views as core_views

app_name = 'core'

urlpatterns = [
    path('', core_views.home, name='home'),
]
