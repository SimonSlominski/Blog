from django.db import models
from django.core.urlresolvers import reverse

from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'rough_copy'),
        ('published', 'released'),
    )

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)
        """ It's important to add ',' (comma) after ordering field. Otherwise, you will get an error.
        blog.Post: (models.E014) 'ordering' must be a tuple or list (even if you want to order by only one field).
        """

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug}) # URL visible as slug
        # return reverse('blog:post_detail', kwargs={'pk': self.pk}) # URL visible as pk/id

