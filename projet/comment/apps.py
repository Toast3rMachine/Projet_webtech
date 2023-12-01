# comment/apps.py
"""
Module de configuration de l'application Comment.
"""

from django.apps import AppConfig

class CommentConfig(AppConfig):
    """
    Configuration de l'application Comment.

    Cette classe représente la configuration de l'application Comment.
    Elle est chargée automatiquement par Django lors du démarrage de l'application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comment'
