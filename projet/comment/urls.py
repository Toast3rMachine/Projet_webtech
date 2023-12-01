from django.urls import path
from comment.views import clear_comments, application

urlpatterns = [
    path('clear-comments/', clear_comments, name='clear_comments'),
    path('application/', application, name='application'),
]