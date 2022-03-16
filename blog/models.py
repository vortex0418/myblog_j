from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)   # 글쓴이
    title = models.CharField(max_length=100)                     # 포스트 제목
    content = models.TextField()                                 # 포스트 내용
    pub_date = models.DateTimeField()                            # 작성일
    modify_date = models.DateTimeField(null=True, blank=True)    # 수정일
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                              null=True, blank=True)             # 사진
    category = models.ForeignKey(Category, null=True, blank=True,
                            on_delete=models.SET_NULL)           # 카테고리

    def __str__(self):
        return self.title

# 댓글 모델
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 댓글 글쓴이
    content = models.TextField()                               # 댓글 내용
    pub_date = models.DateTimeField()                          # 댓글 작성일
    modify_date = models.DateTimeField(null=True, blank=True)  # 댓글 수정일
    post = models.ForeignKey(Post, null=True, blank=True,      # 포스트(외래키)
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.content


