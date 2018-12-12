from django.conf.urls import url

from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post_detail'), # URL visible as slug
    # url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'), # URL visible as pk/id
    url(r'^blog/add/$', PostCreateView.as_view(), name='post_create'),

]

