from django import forms
from blog.models import Post, Comment

# 포스트 폼
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'category']
        labels = {
            'title': '제목',
            'content': '내용',
            'photo': '사진',
            'category' : '카테고리'
        }

# 댓글 폼
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': '댓글 내용'}

