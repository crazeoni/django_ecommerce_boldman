from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
	# path('password_change/', views.password_change , name='password_change'),
	path('login/', LoginView.as_view( template_name='users/login.html'), name='login'),
	path('logout/', views.logout_view, name='logout'),
	# path('activate/<uidb64>/<token>/', views.activate, name='activate'),
	path('register/', views.register, name='register'),
	# path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html')),
	# path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html')),
	# path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html')),
	# path('reset/<uidb64>/<token>/',
         # auth_views.PasswordResetConfirmView.as_view(
             # template_name='users/password_reset_confirm.html'
         # ),
         # name='password_reset_confirm'),
    
]
