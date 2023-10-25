from django.shortcuts import render, redirect
from .models import Board, Comment
from .forms import BoardForm, CommentForm

# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards,
    }
    return render(request, 'boards/index.html', context)


def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.auth = request.user
            form.save()
            return redirect('boards:index')
    else:
        form = BoardForm()
    context = {
        'form':form,
    }
    return render(request, 'boards/create.html', context)


def detail(request, pk):
    board = Board.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = board.comment_set.all()
    context = {
        'board': board,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'boards/detail.html', context)


def update(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm(instance=board)
    context = {
        'board': board,
        'form': form,
    }
    return render(request, 'boards/update.html', context)


def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('boards:index')


def create_comment(request, pk):
    board = Board.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.board = board
        comment.user = request.user
        comment_form.save()
        return redirect('boards:detail', board.pk)
    context = {
        'board': board,
        'comment_form': comment_form,
    }
    return render(request, 'boards/detail.html', context)


def delete_comment(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('boards:detail', board_pk)


def update_comment(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('boards:detail', board_pk)
    else:
        comment_form = CommentForm(instance=comment)
    context = {
        'comment_form': comment_form,
    }
    return render(request, 'boards/detail.html', context)