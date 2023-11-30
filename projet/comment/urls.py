"""
URL configuration for webtech_projet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# comment/urls.py
from django.urls import path
from .views import CommentListView, CommentDetailView, clear_comments

app_name = 'comment'

urlpatterns = [
    path('list/', CommentListView.as_view(), name='comment_list'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('clear-comments/', clear_comments, name='clear_comments'),
    # Ajoutez d'autres URL patterns au besoin
]

