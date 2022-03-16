from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment, Category

def postlist(request):
    #블로그 홈
    post_list = Post.objects.order_by('-pub_date')

    # 페이지 처리
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    page_obj = paginator.get_page(page)
    context = {
        'post_list':page_obj,
        'categories': Category.objects.all()
    }
    return render(request, 'blog/post_list.html', context)

def detail(request, pk):
    # 블로그 상세 페이지
    #post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, pk=pk)  #url경로 오류 처리
    context = {
        'post':post,
        'categories': Category.objects.all(),
    }
    return render(request, 'blog/post_detail.html', context)

def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'post_list' : Post.objects.filter(category=category),
        'categories' : Category.objects.all(),
        'category' : category
    }
    return render(request, 'blog/post_list.html', context)

@login_required(login_url='common:login')
def post_create(request):
    # 글 쓰기
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user   #작성자 - 세션 발급
            form.pub_date = timezone.now()
            form.modify_date = timezone.now()
            form.save()
            return redirect('blog:postlist')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)

# 포스트 삭제
@login_required(login_url='common:login')
def post_delete(request, pk):
    # 포스트 삭제
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:postlist')

@login_required(login_url='common:login')
def post_modify(request, pk):
    # 포스트 수정
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.modify_date = timezone.now()
            post.save()
            return redirect('blog:detail', pk=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)

@login_required(login_url='common:login')
def comment_create(request, pk):
    # 댓글 등록
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  #세션
            comment.pub_date = timezone.now()
            comment.post = post   # 포스트(외래키)
            comment.save()
            return redirect('blog:detail', pk=post.id)
    else:
        form = CommentForm()
    context = {'form':form}
    return render(request, 'blog/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    # 댓글 삭제
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('blog:detail', pk=comment.post.id)

@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    # 댓글 수정
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('blog:detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form':form}
    return render(request, 'blog/comment_form.html', context)
