from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):

    CATEGORY_CHOICES = (
    ('mobile','MOBILE'),
    ('software', 'SOFTWARE'),
    ('game','GAME'),
    ('space','SPACE'),
    ('science','SCIENCE'),
    ('social media','SOCIAL MEDIA'),
    ('equipment','EQUIPMENT'),
   
    
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=200, choices = CATEGORY_CHOICES)
    description = models.TextField()
    author = models.CharField(max_length=100)
    published = models.DateField(default=timezone.now())
    image = models.FileField(null=True, blank=True )
    views = models.CharField(blank=True, max_length=100)
  

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('spider:detail', kwargs={'id': self.id})

class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    comment = models.TextField()
    date = models.DateField(default=timezone.now())
