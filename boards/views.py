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
        game_info = list(soup.find_all(class_='standard_tabelle'))
        matches = game_info[0].select("tr")
        match_ls = []
        for match in matches:
            match_info = match.select('td')
            tmp = []
            for info in match_info:
                if info.text:
                    tmp.append(info.text)
                    if len(tmp) == 5:
                        break
                else:
                    tmp.append('-')
                
            match_ls.append(tmp)
        
        ranks = game_info[1].select("tr")
        rank_info = []
        for rank in ranks[1:]:
            rank_tmp = rank.select('td')
            tmp = [rank_tmp[0].text,
                    rank_tmp[1].find('img').get('src'),
                    rank_tmp[2].text,
                    rank_tmp[3].text,
                    rank_tmp[4].text,
                    rank_tmp[5].text,
                    rank_tmp[6].text,
                    rank_tmp[7].text,
                    ]
            rank_info.append(tmp)
    context = {
        'match_ls': match_ls,
        'rank_info': rank_info,
    }
    return render(request, 'boards/test.html', context)