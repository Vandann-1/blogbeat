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
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return self.user.username
    
#comments features crud operation    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')  #
    comments= models.TextField()
    Create_at = models.DateTimeField()
    
#repleies comments features  crud operation 
class Replycmt(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    replies = models.CharField(max_length=500)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='commentss')  
    


        
        

        