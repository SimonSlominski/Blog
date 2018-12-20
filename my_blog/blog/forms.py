from django import forms
from django.utils.text import slugify

from .models import Post, Comment


class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'body',
            'tags'
        ]


    def save(self):
        # Slug auto-creation based on the title
        instance = super(PostModelForm, self).save()
        instance.slug = slugify(instance.title)
        instance.save()
        return instance


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'name',
            'body',
        ]



