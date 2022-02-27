from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views, htmx_views

app_name = 'user'


urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]

htmx_urlpatterns = [
    path('check-username/', htmx_views.check_username, name='check-username'),
]

urlpatterns += htmx_urlpatterns