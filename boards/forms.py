from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta():
        model = Board
        fields = ['title', 'content', 'image',]


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('content',)
    

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # content 필드를 보이게 하려면 아래와 같이 설정
        self.fields['content'].widget = forms.Textarea(attrs={'rows': 2})