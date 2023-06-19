from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suggestion(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255,default='')
    email = models.EmailField(default='')

    def __str__(self):
        return self.content