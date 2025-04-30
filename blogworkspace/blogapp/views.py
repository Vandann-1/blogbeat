from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog ,  Comment , Savedblog
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required   #its basic use is that to login to auth
from django.http import HttpResponseRedirect
from django.urls import reverse





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
    blogs=Blog.objects.filter(user=request.user).order_by("created_at")
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





    
from django.http import JsonResponse
from .models import Blog




@login_required
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    liked = False

    if request.user in blog.likes.all():
        blog.likes.remove(request.user)
        liked = False
    else:
        blog.likes.add(request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': blog.likes.count()
    })


@login_required
def add_comment(request, blog_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        blog = Blog.objects.get(id=blog_id)
        Comment.objects.create(blog=blog, content=content, user=request.user)
        return JsonResponse({'success': True})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    # Checks if the current user has already liked the blog
    user_has_liked = blog.likes.filter(user=request.user).exists()

    return render(request, 'blogdetails.html', {
        'blog': blog,
        'user_has_liked': user_has_liked,
    })


def savedblog(request, blog_id):
    if not request.user.is_authenticated:
        return HttpResponseForbidden('Unauthorized Access')

    blog = get_object_or_404(Blog, id=blog_id)
    Savedblog.objects.create(blog=blog, user=request.user)
    return redirect('home')    
 
@login_required
def saved_blogs_view(request):
    
    saved_blogs = Savedblog.objects.filter(user=request.user).order_by('-timestamp')  # ✅ Correct
    return render(request, 'savebg.html', {'saved_blogs': saved_blogs})

@login_required
def remove_saved_blog(request, blog_id):
    blog = get_object_or_404(Savedblog, id=blog_id, user=request.user)
    blog.delete()
    return redirect('saved_blogs')        


# views.py
import openai
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

openai.api_key = "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"  # Replace this with your key

@csrf_exempt
def ai_chat(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            user_msg = body.get("message", "")

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_msg}]
            )

            reply = response.choices[0].message.content.strip()
            return JsonResponse({"reply": reply})
        except Exception as e:
            return JsonResponse({"reply": "Oops! Something went wrong."})
    return JsonResponse({"reply": "Invalid request."})
