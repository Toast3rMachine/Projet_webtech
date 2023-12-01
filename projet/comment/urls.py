from django.urls import path
from comment.views import application

urlpatterns = [
    path('application/', application, name='application'),
]