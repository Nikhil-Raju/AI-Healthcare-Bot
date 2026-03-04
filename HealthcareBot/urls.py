from django.contrib import admin
from django.urls import path
from bot_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login_home'), # This matches name='login_home' in your error log
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('chat/', views.chat_view, name='chat'),
    path('logout/', views.logout_view, name='logout'),
    path('api/chat/', views.chat_api, name='chat_api'),
]