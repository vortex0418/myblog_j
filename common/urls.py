from django.contrib.auth import views as auth_views
from django.urls import path, include
from common import views

app_name = 'common'

urlpatterns = [
    # 로그인
    path('login/', auth_views.LoginView.as_view(
        template_name = 'common/login.html'), name='login'),
    # 로그아웃
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 회원 가입
    path('signup/', views.signup, name='signup')
]