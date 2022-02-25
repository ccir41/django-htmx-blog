from django.urls import path

from . import views

app_name = 'core'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('post/', views.PostView.as_view(), name='post'),
]