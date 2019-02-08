from django.conf.urls import include, url
from django.contrib import admin
from post.views import blog
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # Examples:
    # url(r'^$', 'spiders.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', blog, name='home'),
    url(r'^spider/', include('post.urls', namespace="spider")),
    url(r'^dashboard/', include('post.urls', namespace="dashboard")),
  
  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
