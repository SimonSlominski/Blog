from django.conf.urls import url

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
    post_share, TagListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagListView.as_view(), name='tagged'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post_detail'), # URL visible as slug
    # url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'), # URL visible as pk/id
    url(r'^blog/add/$', PostCreateView.as_view(), name='post_create'),
    url(r'^update/(?P<slug>[-\w]+)/$', PostUpdateView.as_view(), name='post_update'),
    url(r'^delete/(?P<slug>[-\w]+)/$', PostDeleteView.as_view(), name='post_delete'),
    url(r'^(?P<slug>[-\w]+)/share/$', post_share, name='post_share'),

]

