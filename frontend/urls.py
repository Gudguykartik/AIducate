from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

app_name = 'frontend'

urlpatterns = [
    # Frontend pages
    path('', views.home, name='home'),  # Home page after login
    path('paths/', views.path, name='paths'),
    path('progress/', views.progress, name='progress'),
    
    # Authentication endpoints
    path('register/', views.register, name='register'),
    path('login/', views.login, name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # User data endpoints
    path('user/progress/', views.get_user_progress, name='user_progress'),
    path('user/skills/', views.get_user_skills, name='user_skills'),
]