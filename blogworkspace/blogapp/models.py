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
    comment= models.CharField(max_length=132, null=True , blank=True)
    is_recurring = models.BooleanField(default=False, null=True , blank=True,choices=(('Daily','daily'),('Monthly','monthly'), ('Weekly','weekly')))
    custom_choices= models.DateTimeField(null=True, blank=True)

    
    def __str__(self):
        return f'{self.title} - {self.user.username}'
   
    class Meta:
        db_table="Blogs"    #to change table name in  sql table
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return self.user.username
    
#comments features crud operation    

class Comment(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




    
#repleies comments features  crud operation 
class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    replies = models.CharField(max_length=500)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='commentss')
    


class SavedBlog(models.Model):   #for saved blog like insta
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blog')  # Prevent duplicate saves
        
        
        

class BlogPost(models.Model):    #likes
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()        

    


        
        

        