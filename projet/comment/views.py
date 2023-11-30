# views.py
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Comment
from .forms import ArticleForm, MyCommentForm 

class CommentForm(MyCommentForm):
    class Meta:
        model = Comment
        fields = ['content']

def application(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('comment_list')
    else:
        form = ArticleForm()

    return render(request, 'comment/application.html', {'form': form})

class CommentListView(View):
    template_name = 'comment/comment_list.html'

    def get(self, request):
        comments = Comment.objects.all()
        return render(request, self.template_name, {'comments': comments})

class CommentDetailView(View):
    template_name = 'comment/comment_detail.html'

    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        return render(request, self.template_name, {'comment': comment})

def clear_comments(request):
    try:
        deleted_count, _ = Comment.objects.all().delete()
        print("Deleted count:", deleted_count)
        deleted_count = int(deleted_count)
        messages.success(request, f'Tous les commentaires ont été supprimés avec succès. Nombre de commentaires supprimés : {deleted_count}')
    except Exception as e:
        print(f"Error: {str(e)}")
        messages.error(request, f'Une erreur s\'est produite lors de la suppression des commentaires : {str(e)}')