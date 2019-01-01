from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        """ Return a collection of objects that will be included in the sitemap. """
        return Post.published.all()

    def lastmod(self, obj):
        """ Set the date and time of the last modification of the given object. """
        return obj.publish

