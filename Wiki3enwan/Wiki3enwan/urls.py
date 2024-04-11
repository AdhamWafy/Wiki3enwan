from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from sitemaps.sitemap import enwaanSitemap

sitemaps = {
    'enwaans':enwaanSitemap,
}

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('anaween.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]