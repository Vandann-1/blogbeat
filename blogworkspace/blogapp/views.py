from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog , Savedblog
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required   #its basic use is that to login to auth




# Create your views here.


@login_required    #its means we need to login to access this view
def addblog(request):
    if request.method == 'POST':
       title=request.POST.get("title")  
       description=request.POST.get("description")  
       blog_image=request.FILES["blog_image"]     # for image upload  we want to use .FILES not requeried POST
       
       blog=Blog()      # its a object
       blog.title=title
       blog.description=description
       blog.blog_image=blog_image
       blog.user=request.user
       blog.save()      #save method to save the data in database which is in models.py and made up by me
       return redirect('home')
       
    else:
        return render(request,"addblog.html")    
        
        

# changes
@login_required
def viewBg(request, bg_id):
    blog = get_object_or_404(Blog, id=bg_id)
    # comments=blog.comments.all()
    # print("FOUND COMMENTS:",comments)
    # print(f'foundedblog{blog}')
    return render(request, "vb.html",{"blog": blog,})





#-----------------------------------------------------------------------------------
@login_required
def myblog(request):
    blogs = Blog.objects.filter(user=request.user)
    return render(request, "myblog.html", {"blogs": blogs})



    
    
@login_required
def delete_blog(request, bg_id):
    blog = get_object_or_404(Blog, id=bg_id)
    blog.delete()
    return redirect('myblog')

@login_required
def edit_blog(request, bg_id):
    blog = get_object_or_404(Blog, id=bg_id)

    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        blog_image = request.FILES.get("blog_image")  # Use .get() to avoid error

        blog.title = title
        blog.description = description
        
        if blog_image:
            blog.blog_image = blog_image  #blog img

        blog.save()
        return redirect('myblog')

    return render(request, "editblog.html", {"blog": blog})
    
#-------------------------------------------------------------------------


    
def is_reccuring(request,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request,"is_recc.html",{'blog':blog})


def Userprofile(request):
    blogs=Blog.objects.filter(user=request.user).order_by("create_at")
    return render(request, 'profile.html',{"blogs":blogs})

@login_required
def editpf(request):
    user = request.user
    if request.method == 'POST':
       
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        first_name = user.first_name
        user.save()   # To save the changes/update
        
        return redirect('profile')
    return render(request, 'editpf.html',{'user':user} )
    
# COMMENT FROM NEW_FEATURE BRANCH
from django.views import View

# class SaveBlogsOnPorfileView(View):
#     pass 

# --03e0edededwe933933237777733332233e



# for savedblog =============================================
@login_required
def toggle_save_blog(request, blog_id):
    """Save or Unsave a blog post"""
    blog = get_object_or_404(Blog, id=blog_id)
    
    # if request.user in blog.saved_by.all():
    if Savedblog.objects.filter(user=request.user,blog =blog).exists():

        Savedblog.objects.filter(user=request.user,blog =blog).delete()
        
        
        print(f" Unsaved: {blog.title} by {request.user}")  # Debugging
        return JsonResponse({"message": "Blog unsaved", "saved": False})
    else:
        # blog.saved_by.add(request.user)
        Savedblog.objects.create(user=request.user, blog=blog)
        
        print(f" Saved: {blog.title} by {request.user}")  # Debugging
        return JsonResponse({"message": "Blog saved", "saved": True})


#  View for rendering the Saved Blogs Page
@login_required
def saved_blogs(request):
    pass
    # saved_blogs = request.user.saved_blogs.all()  # Check if this returns blogs
    # print("Saved Blogs:", saved_blogs)  

    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    #     data = {
    #         "saved_blogs": [
    #             {
    #                 "id": blog.id,
    #                 "title": blog.title,
    #                 "description": blog.description,
    #                 "image_url": blog.blog_image.url if blog.blog_image else "",
    #                 "author": f"{blog.user.first_name} {blog.user.last_name}",
    #             }
    #             for blog in saved_blogs
    #         ]
    #     }
    #     return JsonResponse(data)

    # return render(request, "saved_blogs.html", {"blogs": saved_blogs})
    
