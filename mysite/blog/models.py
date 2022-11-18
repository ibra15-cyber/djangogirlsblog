from time import time
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): #inherits models.Model to define the fields
    #properties
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #characters or methods
    def publish(self):
        published_date = time.now() #time.now given to published
        save()

    def __str__(self):
        return self.title

