from django.urls import path
from django.contrib.sitemaps.views import sitemap

# from .sitemaps import PostSiteMap, PostTypeSiteMap
from . import views

# sitemaps = {
#     'posts': PostSiteMap,
#     'types': PostTypeSiteMap
# }

urlpatterns = [
 
    path('', views.index, name='index'),
    path('pickwinner', views.pickwinner, name='pickwinner'),

    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

 
]
