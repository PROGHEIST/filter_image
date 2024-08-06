# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import LoginView, SignUpView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('output/', views.output, name='output'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', LogoutView.as_view(), name='logout'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
