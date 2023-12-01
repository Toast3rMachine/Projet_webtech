# comment/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Comment
from .forms import ArticleForm, CommentForm

class CommentForm(CommentForm):
    """
    Formulaire pour les commentaires.
    """
    class Meta:
        model = Comment
        fields = ['content']

class CommentView(View):
    """
    Vue pour gérer les commentaires.
    """

    def get(self, request):
        """
        Gère la requête GET.
        """
        return HttpResponse("Hello, this is a GET request.")

    def post(self, request):
        """
        Gère la requête POST.
        """
        return HttpResponse("Hello, this is a POST request.")

def application(request):
    """
    Vue pour gérer l'application.
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = ArticleForm()

    return render(request, 'comment/application.html', {'form': form})

def clear_comments(request):
    """
    Vue pour supprimer tous les commentaires.
    """
    try:
        deleted_count, _ = Comment.objects.all().delete()
        print("Deleted count:", deleted_count)
        deleted_count = int(deleted_count)
        messages.success(request, f'Tous les commentaires ont été supprimés avec succès. Nombre de commentaires supprimés : {deleted_count}')
    except Exception as e:
        print(f"Error: {str(e)}")
        messages.error(request, 'Une erreur s\'est produite lors de la suppression des commentaires.')

def your_view(request):
    """
    Votre vue personnalisée.
    """
    try:
        # Ajoutez votre logique de vue ici
        pass
    except Exception as e:
        print(f"Error: {str(e)}")
        messages.error(request, 'Une erreur s\'est produite.')

# Ajoutez d'autres vues au besoin
