from django.conf.urls import include, url
from django.contrib import admin
from post.views import home_view,lazy_load_posts
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # Examples:
    # url(r'^$', 'spiders.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view, name='home'),
    url(r'^lazy_load_posts/$', lazy_load_posts, name='lazy_load_posts'),
  
  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
