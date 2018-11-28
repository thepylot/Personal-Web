from django.db import models

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
    datetime = models.DateTimeField(auto_now_add=True)
    image = models.FileField(null=True, blank=True )


