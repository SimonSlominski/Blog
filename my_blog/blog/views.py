from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostModelForm, EmailPostForm
from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 3


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


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostModelForm
    slug_field = 'slug'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(PostUpdateView, self).form_valid(form)

    def get_success_url(self):
        return '/blog'


class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return '/blog'


def post_share(request, slug):
    # Taking a post based on its slug.
    post = get_object_or_404(Post, slug=slug)
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # Send email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n {}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comment'])
            recipient = cd['to']

            send_mail(subject, message, 'simon.slominski@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
        recipient = False
    return render(request, 'share.html', {'post':post, 'form': form, 'sent': sent, 'recipient': recipient})

