from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Recipe, Comment
from .forms import CommentForm
from django.core.paginator import Paginator
from allauth.account.views import SignupView


def home(request):
    return render(request, 'index.html')


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe.html', {'recipes': recipes})


def recipe_like(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if not request.user.is_authenticated:
        return redirect('account_login')

    if request.user in recipe.likes.all():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)

    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        return redirect('recipe_content', recipe_id=recipe.id)


def recipe_content(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    comments = recipe.comment_set.all().order_by('-created_on')
    paginator = Paginator(comments, 4)  # Show 4 comments per page

    page = request.GET.get('page')
    comments = paginator.get_page(page)

    form = CommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.recipe = recipe
                comment.user = request.user
                comment.save()
                return redirect('recipe_content', recipe_id=recipe.id)
        else:
            return redirect('account_login')
    return render(request,
                  'recipe_content.html',
                  {'form': form, 'recipe': recipe, 'comments': comments})


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user and not request.user.is_staff:
        return redirect('recipe_content', recipe_id=comment.recipe.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('recipe_content', recipe_id=comment.recipe.id)
    else:
        form = CommentForm(instance=comment)

    return render(request,
                  'edit_comment.html', {'form': form, 'comment': comment})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user and not request.user.is_staff:
        return redirect('recipe_content', recipe_id=comment.recipe.id)

    if request.method == 'POST':
        comment.delete()
        return redirect('recipe_content', recipe_id=comment.recipe.id)

    return render(request, 'delete_comment.html', {'comment': comment})
