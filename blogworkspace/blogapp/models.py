from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
# class Blog(models.Model):
#     title = models.CharField(max_length=50)
#     description=models.CharField(max_length=200)
#     create_at=models.DateField(auto_now_add=True)
#     blog_image=models.ImageField(upload_to="blogimages/")
#     user=models.ForeignKey(User,on_delete=models.CASCADE) #it means delete all user blog
#     custom_date=models.DateTimeField(null=True,blank=True)
#     custom_choices= models.DateTimeField(null=True, blank=True)
# for savedblog

     
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()  # Changed to TextField for longer descriptions
     # Changed to DateTimeField for more precision
    blog_image = models.ImageField(upload_to="blogimages/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # it means delete all user blog
    custom_date = models.DateTimeField(null=True, blank=True)
    custom_choices = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now) 
    likes = models.ManyToManyField(User, related_name='liked_blogs', blank=True)

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f'{self.title} - {self.user.username}'

    class Meta:
        db_table = "Blogs"  # to change table name in sql table
        ordering = ['-created_at']  # Added ordering by creation date

# Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return self.user.username

    def get_profile_picture(self):
        if self.profile_picture:
            return self.profile_picture.url
        return '/static/img/default.jpg'  # Added a method to get the profile picture URL

        
 
 
        
#profile 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return self.user.username
    






#  for comment
class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"



    


        
        

        