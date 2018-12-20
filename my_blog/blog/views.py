from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from .forms import PostModelForm, EmailPostForm, CommentForm
from .mixins import TagMixin
from .models import Post, Comment



class PostListView(TagMixin, ListView):
    model = Post
    paginate_by = 3


class TagListView(TagMixin, ListView):
    model = Post
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        slug = self.kwargs.get('slug')
        return reverse('blog:post_detail', kwargs={'slug': slug})

    def get_context_data(self, **kwargs):
        contex = super(PostDetailView, self).get_context_data(**kwargs)
        contex['form'] = CommentForm(initial={'post': self.object})
        return contex

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        instance.post = self.object
        instance.save()
        return super(PostDetailView, self).form_valid(form)


class PostCreateView(TagMixin, CreateView):
    model = Post
    form_class = PostModelForm

    def get_success_url(self):
        return '/blog'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(PostCreateView, self).form_valid(form)


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

