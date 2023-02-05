from django.shortcuts import render
from .models import Blogpost 
# Create your views here.
from django.http import HttpResponse
import datetime
from django.contrib import messages


def  index(request):
    
    return render(request, 'blog/index.html')

def home(request):
    myposts= Blogpost.objects.all()
    time= datetime.datetime.now()
    print(time.strftime("%y-%m-%d %H:%M:%S"))
    
    return render(request, 'blog/home.html', {'myposts': myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',
                  {'post':post})

def search(request):
   query=request.GET.get('query','')
   print(query)
   if len(query)>78:
    allPosts=Blogpost.objects.none()
   else:
    allPostsTitle= Blogpost.objects.filter(tilte__icontains=query)
    allPostshead0= Blogpost.objects.filter(head0__icontains=query)
    allPostschead0= Blogpost.objects.filter(chead0__icontains=query)
    allPostshead1= Blogpost.objects.filter(head1__icontains=query)
    allPostschead1= Blogpost.objects.filter(chead1__icontains=query)
    allPostshead2= Blogpost.objects.filter(head2__icontains=query)
    allPostschead2 =Blogpost.objects.filter(chead2__icontains=query)
    allPostsdate=blogpost.objects.filter(date__icontains=query)
    allPosts=  allPostsTitle.union(allPostshead0,allPostschead0,allPostshead1,allPostschead1,allPostshead2,allPostschead2,allPostsdate)
   if allPosts.count()==0:
    messages.warning(request, "No search results found. Please refine your query.")
   params={"allPosts":allPosts, 'query': query}
   return render(request,'blog/search.html', params)
    

# def postComment(request):
#     if request.method == "POST":
#         comment=request.POST.get('comment')
#         user=request.user
#         postSno =request.POST.get('postSno')
#         post= Post.objects.get(sno=postSno)
#         comment=BlogComment(comment= comment, user=user, post=post)
#         comment.save()
#         messages.success(request, "Your comment has been posted successfully")
        
#     return redirect(f"/blog/{post.slug}")