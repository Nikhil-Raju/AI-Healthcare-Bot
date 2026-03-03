from django.contrib import admin
from django.urls import path
from bot_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login_home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'), # Added slash
    path('chat/', views.chat_view, name='chat'),   # Added slash
    path('logout/', views.logout_view, name='logout'),
    path('api/chat/', views.chat_api, name='chat_api'),
]