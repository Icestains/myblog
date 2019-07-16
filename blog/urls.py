# from django.conf.urls import url
from django.urls import path
from . import views

from blog.feeds import AllPostRssFeed

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<pk>', views.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>', views.ArchivesView.as_view(), name='archives'),
    path('category/<name>', views.CategoryView.as_view(), name='category'),
    path('tag/<pk>', views.TagView.as_view(), name='tag'),
    path('all/rss/', AllPostRssFeed(), name='rss'),
]
