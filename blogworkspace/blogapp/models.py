from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    create_at=models.DateField(auto_now_add=True)
    blog_image=models.ImageField(upload_to="blogimages/")
    user=models.ForeignKey(User,on_delete=models.CASCADE) #it means delete all user blog
    is_recurring=models.BooleanField(default=False,null=True,blank=True)
    custom_date=models.DateTimeField(null=True,blank=True)
    
   
    class Meta:
        db_table="Blogs"    #to change table name in 
        
class saved_Blog(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE) #it means delete all user blog
    saved_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together =('user','blog')
        
        

        