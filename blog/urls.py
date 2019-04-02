# from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<title>', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>', views.archives, name='archives'),
    path('category/<name>', views.category, name='category'),
]
