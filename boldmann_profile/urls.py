from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'starrprofile'
urlpatterns = [
	# path('<slug>/', views.view_user_profile, name ='view_user_profile'),
	path('create_profile', views.create_profile, name='create_profile'),
	path('view_profile/', views.view_profile, name ='view_profile'),
	path('view_profile/edit_profile/', views.edit_profile, name ='edit_profile'),
	path('profile/', views.profile_view, name='profile_view'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

