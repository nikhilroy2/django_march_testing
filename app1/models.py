from django.db import models
from django.utils import timezone
# Create your models here.
class URL(models.Model):
    full_url = models.TextField()
    hash = models.TextField(unique=True)
    class Meta:
        db_table = 'url_shortener'

class CRUD_Create(models.Model):
    firstName = models.CharField(max_length=25, default="")
    lastName = models.CharField(max_length=25, default="")
    email = models.EmailField(max_length=55, default="")
    date = models.DateTimeField(auto_created=True, default=timezone.now)
    class Meta:
        db_table = 'crud__create'
    def __str__(self):
        return self.firstName
