from django.views.generic import ListView, DetailView, CreateView

from .forms import PostModelForm
from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostModelForm

    def get_success_url(self):
        return '/blog'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



