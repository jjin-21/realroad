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



import requests
from bs4 import BeautifulSoup as bs
def test(request):
    url = 'https://www.worldfootball.net/schedule/eng-premier-league-2023-2024-spieltag/10/'

    # URL에 GET 요청을 보내서 웹 페이지의 소스를 가져옴
    response = requests.get(url)

    # 응답 상태 코드 확인 (200은 성공을 나타냄)
    if response.status_code == 200:
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = bs(response.text, 'html.parser')
        games = soup.find(class_='standard_tabelle').select("tr")
        game_ls = []
        for game in games:
            game_info = game.find_all(class_='hell')
            tmp = []
            for info in game_info:
                if info.text:
                    tmp.append(info.text)
                else:
                    tmp.append('-')
                if len(tmp) == 5:
                    break
            game_ls.append(tmp)
    context = {
        'game_ls': game_ls,
    }
    return render(request, 'boards/test.html', context)