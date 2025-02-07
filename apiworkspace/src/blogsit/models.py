from django.db import models

# Create your models here.
class stblog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    
    
    class Meta:
        db_table="studentblogs"