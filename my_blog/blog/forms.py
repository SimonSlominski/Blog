from django import forms
from django.utils.text import slugify

from .models import Post


class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'body',
        ]

    def save(self):

        # Slug auto-creation based on the title
        instance = super(PostModelForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()

        return instance
