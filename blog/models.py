from django.db import models

class Blog(models.Model):
    title= models.CharField(max_length=50)
    image= models.URLField(max_length=200)
    body= models.TextField()
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title