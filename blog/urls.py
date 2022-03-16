from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from blog import views

app_name = 'blog'

urlpatterns = [
    # 포스트 목록
    path('', views.postlist, name='postlist'),
    # 포스트 상세 페이지
    path('<int:pk>/', views.detail, name='detail'),
    # 카테고리
    path('category/<str:slug>/', views.category_page, name='category_page'),
    # 포스트 등록
    path('post/create/', views.post_create, name='post_create'),
    # 포스트 삭제
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    # 포스트 수정
    path('post/modify/<int:pk>/', views.post_modify, name='post_modify'),
    # 댓글 등록
    path('comment/create/<int:pk>/', views.comment_create, name='comment_create'),
    # 댓글 삭제
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    # 댓글 수정
    path('comment/modify/<int:comment_id>/', views.comment_modify, name='comment_modify'),
]
