from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from anaween.models import enwaan

class enwaanSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        # Fetch user-added pages from your model (replace with your model name and queryset logic)
        enwaans = enwaan.objects.filter(is_published=True)
        return enwaans

    def location(self, item):
        # Construct the URL for each user-added page using reverse()
        return reverse('enwaan-detail', kwargs={'slug': item.slug})
