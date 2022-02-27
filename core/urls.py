from django.urls import path

from . import views, htmx_views

app_name = 'core'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('post/', views.PostView.as_view(), name='post'),
]

htmx_urlpatterns = [
    path('render-navbar/', htmx_views.render_navbar, name='render-navbar'),
]

urlpatterns += htmx_urlpatterns