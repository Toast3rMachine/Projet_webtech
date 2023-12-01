from django.shortcuts import render
from .models import Comment
from .forms import CommentForm

def application(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            date = form.cleaned_data['date']
            user = request.user

            comment = Comment(content=content, user=user, date=date)
            comment.save()
    else:
        form = CommentForm()

    return render(request, 'comment/application.html', {'form': form})

# def clear_comments(request):
#     try:
#         deleted_count, _ = Comment.objects.all().delete()
#         print("Deleted count:", deleted_count)
#         deleted_count = int(deleted_count)
#         messages.success(request, f'Tous les commentaires ont été supprimés avec succès. Nombre de commentaires supprimés : {deleted_count}')
#     except Exception as e:
#         print(f"Error: {str(e)}")
#         messages.error(request, 'Une erreur s\'est produite lors de la suppression des commentaires.')